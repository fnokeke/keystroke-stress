PAM-PHP, a PHP implementation of PAM.

PAM: The Photographic Affect Meter
Copyright 2010-present
Interaction Design Lab (idl.cornell.edu)
Cornell University (cornell.edu)
JP Pollak (jppollak.com)
Phil Adams (philadams.net)

This code to be used only with the express permission of creators Pollak or Adams.

Reference:
John P. Pollak, Phil Adams, and Geri Gay. 2011. PAM: a photographic affect meter for frequent, in situ measurement of affect. In Proceedings of the 2011 annual conference on Human factors in computing systems (CHI '11). ACM, New York, NY, USA, 725-734. DOI=10.1145/1978942.1979047 http://doi.acm.org/10.1145/1978942.1979047

Usage
-----

The sample file form.php has everything you need. Basically, include the PAM css and js files (requires JQuery), and then call pam_display_form($submit_to) to output PAM. The sample file receipt.php demonstrates how to get PAM output back.

Sample output
-------------

Array
(
    [image_id] => 29
    [cell_id] => 10
    [pam_pa] => 13
    [pam_na] => 8
    [arousal] => 2
    [valence] => 3
)
