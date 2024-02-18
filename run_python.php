<?php
$cmd = "python C:/Users/buildpc.shop/Desktop/speech2/speechtotext.py";
$output = shell_exec($cmd);
$data = json_decode($output, true);
echo $data['text']
?>
