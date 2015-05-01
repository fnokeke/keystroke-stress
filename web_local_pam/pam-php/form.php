<?php
require './pam/config.php';
require('./pam/funcs.php');
$pam_data = pam_process_form($_POST['pam_image_id']);

if (isset($_POST['pam_image_id'])) {
    $image_id = $pam_data[image_id];
    $cell_id = $pam_data[cell_id];
    $pam_pa = $pam_data[pam_pa];
    $pam_na = $pam_data[pam_na];
    $arousal = $pam_data[arousal];
    $valence = $pam_data[valence];

    // save result in a file
    date_default_timezone_set('America/New_York');
    $t = time();
    $current_time = date("Y-m-d H:i:s", $t);

    $result = 
        "time: "     .$current_time  .
", image_id: " .$image_id    . 
", cell_id: "  .$cell_id     . 
", pam_pa: "   .$pam_pa      . 
", pam_na: "   .$pam_na      . 
", arousal: "  .$arousal     .
", valence: "  .$valence     .
"\n";

// Write the contents to the file, 
// using the FILE_APPEND flag to append the content to the end of the file
// and the LOCK_EX flag to prevent anyone else writing to the file at the same time 
$file="../../data/self_report/pam_log.txt";
file_put_contents($file, $result, FILE_APPEND | LOCK_EX);
header("Location: http://localhost:8000/self_report.php");


//$query = "INSERT INTO `logs`(`imageID`, `cellID`, `pam_pa`, `pam_na`, `arousal`, `valence`, `time`) VALUES ('$image_id', '$cell_id', '$pam_pa', '$pam_na', '$arousal', '$valence', CURRENT_TIMESTAMP);";
//$mysqli->query($query);
}
?>

<!-- 1 - afraid - deep red - 8B0000
2 - tense - red - FF0000
3 - excited - orange - FF6600
4 - delighted - yellow - FFFF00
5 - frustrated - deep red - 8B0000
6 - angry - red - FF0000
7 - happy - yellow - FFFF00
8 - glad - green - 33FF33
9 - miserable - 000000
10 - sad - grey - 999999
11 - calm - blue - 19E0FF
12 - satisfied - true blue - 0000FF
13 - gloomy - grey - 999999
14 - tired - violet - 7D26CD
15 - sleepy - violet - 7D26CD
16 - serene - teal - 40E0D0 -->


<!DOCTYPE html>
<html lang="en">
<center>
  <head>
    <meta charset="utf-8">
    <title>PAM-PHP</title>
    <meta name="description" content="TODO">
    <meta name="author" content="TODO">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0"/> <!--320-->
    <meta name="apple-mobile-web-app-capable" content="yes">

    <!-- Le styles -->
    <link href="./pam/pam.css" rel="stylesheet">
    <!-- Le HTML5 shim, for IE6-8 support of HTML elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le fav and touch icons -->
    <link rel="shortcut icon" href="../images/favicon.ico">
    <link rel="apple-touch-icon" href="./images/apple-touch-icon.png">
    <link rel="apple-touch-icon" sizes="72x72" href="./images/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="114x114" href="./images/apple-touch-icon-114x114.png">
<link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:200' rel='stylesheet' type='text/css'>
<script>
</script>
  </head>

  <body bgcolor="black">
    <div style="zoom: 2">
    <div class="container">

      <div class="content">
<?php
pam_display_form('./form.php');
?>
      </div>

    </div> <!-- /container -->


    <!-- Le Javascripts -->
    <script src="./pam/jquery.js"></script>
    <script src="./pam/pam.js"></script>
</div>
  </body>
</center>
</html>
