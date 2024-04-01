-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 01, 2024 at 07:50 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `learning_platforms`
--

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `id` int NOT NULL,
  `course_id` int DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `instructor` varchar(100) DEFAULT NULL,
  `duration` int DEFAULT NULL,
  `price` float DEFAULT NULL,
  `status` int DEFAULT NULL,
  `field1` varchar(100) DEFAULT NULL,
  `field2` int DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` varchar(512) DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  `updated_by` varchar(512) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`id`, `course_id`, `title`, `description`, `instructor`, `duration`, `price`, `status`, `field1`, `field2`, `note`, `created_on`, `created_by`, `updated_on`, `updated_by`) VALUES
(1, 1001, 'Python', 'Python for beginers', 'Md. Tamim', 150, 500, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 1002, 'Python2', 'Python for beginers', 'Md. Tamim', 150, 500, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 1003, 'Python3', 'Python for beginers', 'Md. Tamim', 150, 500, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 1004, 'py', 'Python for beginers', 'Md. Tamim', 150, 500, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, 1005, 'py', 'Python for beginers', 'Md. Tamim', 150, 500, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(6, 1006, 'py', 'Python for beginers', 'Md. Tamim', 150, 500, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(7, 1007, 'py', 'Python for beginers', 'Md. Tamim', 150, 500, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(8, 1008, '454', 'Python for beginers', 'Md. Tamim', 150, 500, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(9, 1009, '45xxx4', 'Python for beginers', 'Md. Tamim', 150, 500, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(10, 1010, 'ok', 'Python for beginers', 'Md. Tamim', 150, 500, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `enrollments`
--

CREATE TABLE `enrollments` (
  `id` int NOT NULL,
  `enroll_id` int DEFAULT NULL,
  `student_name` varchar(20) DEFAULT NULL,
  `course_id` varchar(100) DEFAULT NULL,
  `enroll_date` date DEFAULT NULL,
  `status` int DEFAULT NULL,
  `field1` varchar(100) DEFAULT NULL,
  `field2` int DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` varchar(512) DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  `updated_by` varchar(512) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `enrollments`
--

INSERT INTO `enrollments` (`id`, `enroll_id`, `student_name`, `course_id`, `enroll_date`, `status`, `field1`, `field2`, `note`, `created_on`, `created_by`, `updated_on`, `updated_by`) VALUES
(1, 1001, 'Python for beginers', '1001', '2024-04-10', 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `user_id` varchar(20) DEFAULT NULL,
  `user_name` varchar(20) DEFAULT NULL,
  `user_email` varchar(50) DEFAULT NULL,
  `user_mobile` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL,
  `field1` varchar(100) DEFAULT NULL,
  `field2` int DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` varchar(512) DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  `updated_by` varchar(512) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `enrollments`
--
ALTER TABLE `enrollments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_email` (`user_email`),
  ADD UNIQUE KEY `user_mobile` (`user_mobile`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `enrollments`
--
ALTER TABLE `enrollments`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
