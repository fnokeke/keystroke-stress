<?php
if (isset($_POST['submit'])) {
    $pleasant_response = $_POST["pleasant_state"];
    $energy_response = $_POST["energy_state"];
    $stress_response =$_POST["stress_state"]; 

    // save result in a file
    date_default_timezone_set('America/New_York');
    $t = time();
    $current_time = date("Y-m-d H:i:s", $t);

    $result = 
        "time: "     .$current_time  .
", pleasant_state: "   .$pleasant_response      . 
", energy_state: "   .$energy_response      . 
", stress_state: "   .$stress_response      . 
"\n";

// Write the contents to the file, 
// using the FILE_APPEND flag to append the content to the end of the file
// and the LOCK_EX flag to prevent anyone else writing to the file at the same time 
$file="../../data/self_report/ema_web_log.txt";
file_put_contents($file, $result, FILE_APPEND | LOCK_EX);

// redirect to thank you page
header("Location: http://localhost:8000/thank_you.php");
exit();
}
?>


<!DOCTYPE html>
<html lang="en">
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
<style>
body {background-color: black; color: lightgray;font-family:courier;}
h2 {color: white; font-family:courier; }
tr.spaceUnder > td
{
  padding-bottom: 1.5em;
}
label 
{
    display: inline-block;
    text-align: left;
    margin-right: 3em;
}

#Absolute-Center {
  width: 60%;
  height: 70%;
  overflow: auto;
  margin: auto;
  position: absolute;
  top: 0; left: 0; bottom: 0; right: 0;
}

.styled-button-7 {
    background: #00A0D1;
    background: -moz-linear-gradient(top,#00A0D1 0%,#008DB8 100%);
    background: -webkit-gradient(linear,left top,left bottom,color-stop(0%,#00A0D1),color-stop(100%,#008DB8));
    background: -webkit-linear-gradient(top,#00A0D1 0%,#008DB8 100%);
    background: -o-linear-gradient(top,#00A0D1 0%,#008DB8 100%);
    background: -ms-linear-gradient(top,#00A0D1 0%,#008DB8 100%);
    background: linear-gradient(top,#00A0D1 0%,#008DB8 100%);
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#00A0D1',endColorstr='#008DB8',GradientType=0);
    padding:8px 20px;
    color:#cfebf3;
    font-family:'Helvetica Neue',sans-serif;
    font-size:13px;
    border-radius:40px;
    -moz-border-radius:40px;
    -webkit-border-radius:40px;
    border:1px solid #095B7E
}

</style>
  </head>

<center>
  <body>
    <div style="zoom: 1">

<div id="Absolute-Center">
<h2>Rate how you feel right now</h2>
<form name="self_report_form" action="./self_report.php" method="POST" >
<table>
<tr class="spaceUnder">

<td>
<input type="radio" name="pleasant_state" id="very_pleasant" value="very_pleasant"/> 
<label for="very_unpleasant">very unpleasant (negative) </label>
</td>

<td>
<input type="radio" name="pleasant_state" id="slightly_unpleasant" value="slightly_unpleasant"/>
<label for="slightly_unpleasant"> slightly unpleasant</label>
</td>


<td>
<input type="radio" name="pleasant_state" id="neutral" value="neutral"/>
<label for="neutral">neutral</label>
</td>

<td>
<input type="radio" name="pleasant_state" id="slightly_pleasant" value="slightly_pleasant"/>
<label for="slightly_pleasant">slightly pleasant</label>
</td>

<td>
<input type="radio" name="pleasant_state" id="very_pleasant" value="very_pleasant"/>
<label for="very_pleasant">very pleasant (positive)</label>
</td>

</tr>

<tr class="spaceUnder">
<td>
<input type="radio" name="energy_state" id="very_low_energy" value="very_low_energy"/>
<label for="very_low_energy">very low energy (calm)</label>
</td>

<td>
<input type="radio" name="energy_state" id="slightly_low_energy" value="slightly_low_energy"/>
<label for="slightly_low_energy">slightly low energy</label>
</td>

<td>
<input type="radio" name="energy_state" id="neutral" value="neutral"/>
<label for="neutral">neutral</label>
</td>

<td>
<input type="radio" name="energy_state" id="slightly_energetic" value="slightly_energetic"/>
<label for="slightly_energetic">slightly energetic</label>
</td>

<td>
<input type="radio" name="energy_state" id="very_energetic" value="very_energetic"/>
<label for="very_energetic">very energetic (awake)</label>
</td>

</tr>

<tr class="spaceUnder">
<td>
<input type="radio" name="stress_state" id="very_stressed" value="very_stressed"/>
<label for="very_stressed">very stressed (negative)</label>
</td>

<td>
<input type="radio" name="stress_state" id="slightly_stressed" value="slightly_stressed"/>
<label for="slightly_stressed">slightly stressed</label>
</td>

<td>
<input type="radio" name="stress_state" id="neutral" value="neutral"/>
<label for="neutral">neutral</label>
</td>

<td>
<input type="radio" name="stress_state" id="feeling_good" value="feeling_good"/>
<label for="feeling_good">feeling good</label>
</td>

<td>
<input type="radio" name="stress_state" id="feeling_great" value="neutral"/>
<label for="feeling_great">feeling great (positive)</label>
</td>

</tr>
</table>
<input type="submit" value="submit" name="submit" class="styled-button-7">
 </div>
</form>

</div>

</center>
  </body>
</html>
