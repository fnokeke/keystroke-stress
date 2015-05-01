<?php

define('PAM_IMAGES', './pam/pam-images.json');
define('PAM_CELLS', './pam/pam-cells.json');
define('PAM_PROMPT', 'How do you feel right now?');
define('LI_FORMAT', '<li id="%s"><img src="./pam/images-medium/%s" height="80" width="80" alt="pam-image"></li>');
define('PAM_LOAD_MORE', 'You can <a id="pam-load-more" href="#">load more images</a>.');
define('PAM_FORM', '<form id="pam-form" method="post" action="%s"><input id="pam-image-id" name="pam_image_id" type="hidden" value="" /></form>');
// define('PAM_FORM', '<form method="post" action="%s"><input id="pam-image-id" name="pam_image_id" type="hidden" value="" /><input id="pam-submit" type="submit" name="pam" value="Submit" /></form>');
define('PAM_NO_JS', "\n\t<p id=\"pam-no-js\">PAM-PHP requires javascript!</p>\n");

/* print out HTML for PAM grid and form
 *  $submit_to: path to page form should be submitted to
*/
function pam_display_form($submit_to) {
  $pam = pam_build_form($submit_to);
  echo $pam;
}

/* build PAM HTML form */
function pam_build_form($submit_to) {

  // all cell images
  $images = json_decode(file_get_contents(PAM_IMAGES));
  $images = $images->pam_images;

  // confirm clustered by cell_id
  $by_cell = array();
  foreach($images as $img) {
    $key = $img->cell_id;
    if (!isset($by_cell[$key])) {
      $by_cell[$key] = array();
    }
    $by_cell[$key][] = $img;
  }

  // randomly select one image for each cell
  $grid = array();
  foreach($by_cell as $cell) {
    $img = $cell[rand(0, count($cell)-1)];
    $grid[] = $img;
  }

  // wrap in markup
  $pam = sprintf('<div id="pam-widget"><p>%s</p><ul>', PAM_PROMPT);
  foreach ($grid as $img) {
    $pam .= sprintf(LI_FORMAT, $img->id, $img->url);
  }
  $pam .= sprintf('</ul><p>%s</p>', PAM_LOAD_MORE);
  $pam .= sprintf(PAM_FORM, $submit_to);
  $pam .= '</div>';
  $pam .= PAM_NO_JS;
  return $pam;
}

/* return PAM values from pam_image_id */
function pam_process_form($image_id) {
  $cells = json_decode(file_get_contents(PAM_CELLS));
  $images = json_decode(file_get_contents(PAM_IMAGES));
  $cells = $cells->pam_cells;
  $images = $images->pam_images;
  $img = $images[$image_id-1];  // honestly sql should index at 0 too
  $cell = $cells[$img->cell_id-1];
  $pam_pa = round(((5 * $cell->valence_pa) + $cell->arousal - 5) * (16/19), 0);
  $pam_na = round(((5 * $cell->valence_na) + $cell->arousal - 5) * (16/19), 0);
  return array('image_id' => $img->id,
               'cell_id' => $img->cell_id,
               'pam_pa' => $pam_pa,
               'pam_na' => $pam_na,
               'arousal' => $cell->arousal,
               'valence' => $cell->valence_pa);
}

?>
