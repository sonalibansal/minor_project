-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2017 at 11:45 AM
-- Server version: 10.1.9-MariaDB
-- PHP Version: 5.6.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `minorproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `extract`
--

CREATE TABLE `extract` (
  `userid` int(11) NOT NULL DEFAULT '101',
  `emailno` int(11) NOT NULL,
  `date` varchar(50) NOT NULL,
  `address` text NOT NULL,
  `time` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `extract`
--

INSERT INTO `extract` (`userid`, `emailno`, `date`, `address`, `time`) VALUES
(101, 1, '14 January 017', 'Delhi, India', ''),
(101, 2, '10 January 2017', 'Kashmere Gate ,Delhi, India', ''),
(101, 3, '19 May 2017', 'Rajouri Garden ,Delhi, India', ''),
(101, 4, '5 July 2017', 'Kilash Colony ,Delhi, India', ''),
(101, 5, '10 January 2017', 'Lal Qila ,Delhi, India', '');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `userid` int(11) NOT NULL,
  `username` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `extract`
--
ALTER TABLE `extract`
  ADD UNIQUE KEY `emailno` (`emailno`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `extract`
--
ALTER TABLE `extract`
  MODIFY `emailno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
