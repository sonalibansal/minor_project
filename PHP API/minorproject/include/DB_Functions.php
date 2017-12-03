<?php
 
class DB_Functions {
 
    private $conn;
 
    // constructor
    function __construct() {
        require_once 'include/DB_Connect.php';
        // connecting to database
        $db = new Db_Connect();
        $this->conn = $db->connect();
    }
 
    
    public function getUsername ($userid){
        $stmt = $this->conn->prepare("SELECT username FROM user WHERE userid = ?");
 
        $stmt->bind_param("s", $userid);
 
        if ($stmt->execute()) {
            $username = $stmt->get_result()->fetch_assoc();
            $stmt->close();
            //print_r($username);
            return $username['username'];

        }
        else
            return false;
    }

    public function getUserDataById($userid){

        $stmt = $this->conn->prepare("SELECT * FROM extract WHERE userid = ?");
 
        $stmt->bind_param("s", $userid);
 
        if ($stmt->execute()) {
            $user = $stmt->get_result()->fetch_all();
            $stmt->close();

            //print_r($user);
            return $user;

        } else {
            return false;
        }
    }
}
 
?>