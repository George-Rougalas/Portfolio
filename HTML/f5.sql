-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Εξυπηρετητής: 127.0.0.1
-- Χρόνος δημιουργίας: 09 Ιαν 2022 στις 10:17:57
-- Έκδοση διακομιστή: 10.4.22-MariaDB
-- Έκδοση PHP: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Βάση δεδομένων: `persona`
--

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `f5`
--

CREATE TABLE `f5` (
  `name` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `sex` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `album` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `comments` text CHARACTER SET utf8 DEFAULT NULL,
  `dislike` text CHARACTER SET utf8 DEFAULT NULL,
  `lyrics` text CHARACTER SET utf8 DEFAULT NULL,
  `review` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Άδειασμα δεδομένων του πίνακα `f5`
--

INSERT INTO `f5` (`name`, `sex`, `album`, `comments`, `dislike`, `lyrics`, `review`) VALUES
('desp', 'on', ',Please Please Me (1963)', 'vcncxn', 'xgfnfgxn', 'ngfxn', 2),
('bgfbgfb', '', ',Beatles For Sale (1964)', 'hgdhdtrh', 'strhdrt', 'hdrtydrt', 3),
('bgfbngf', '', ',Yellow Submarine (1969)', 'freghtrh', 'trhtydehe', 'tyhteyh', 4),
('desp', 'on', ',Please Please Me (1963)', ' ghcjmndghc', 'mncghnmgchnmfgxn xfg', 'ngfxn fxgn', 5),
('rthtrh', '', ',Beatles For Sale (1964)', 'rgfbdfsh', 'bgsdhfgbsdrgh', 'resghaer', 3),
('bgfbngf', '', ',Please Please Me (1963)', 'hfghfdhy', 'jhtdyjn', 'ghjngh', 2),
('Δέσποινα Νικόλαος Δεσποινίδη', 'on', ',A Hard Day’s Night (1964)', 'trhsyrdt', 'trhshtr', 'trsystr', 3);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
