<?php
require_once 'include/DB_Functions.php';
$db = new DB_Functions();
 
// json response array
$response = array("error" => FALSE);
 
if (isset($_GET['userid'])) {
 
    // receiving the post params
    $userid = $_GET['userid'];
     
    // get the username by userid 
    $name= $db->getUsername($userid);
    
    $contentArray = $db->getUserDataById($userid);
    $number = count($contentArray);
    //print_r($contentArray);
 
    if ($contentArray != false) {
        
        $response["error"] = FALSE;
        $response["userid"] = $contentArray[0][0];
        $response["name"] = $name;

        for ($i=0; $i< $number; $i++){

        	$response["content"][$i] = array("emailno"=>$contentArray[$i][1],"date"=>$contentArray[$i][2],"address"=>$contentArray[$i][3], "time"=>$contentArray[$i][4]);
            

    	}
            echo json_encode($response);
     } 
     
    else {
        // user is not found with the credentials
        $response["error"] = TRUE;
        $response["error_msg"] = "employee_id not correct. Please try again!";
        echo json_encode($response);
    }
} else {
    // required post params is missing
    $response["error"] = TRUE;
    $response["error_msg"] = "Required parameter is missing!";
    echo json_encode($response);
}
?>