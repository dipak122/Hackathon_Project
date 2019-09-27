<?php
$to = "dipak717gautam@gmail.com";
$subject = "response from website";
$message = "hii i m from dipak";
$headers="raviraj@digitechreviews.com";
if (mail($to,$subject, $message ,$headers )){
    echo "done";

}
else{
echo "fail";
}
?>