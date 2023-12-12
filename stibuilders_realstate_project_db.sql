-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 25, 2023 at 11:53 AM
-- Server version: 8.0.34
-- PHP Version: 8.1.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stibuilders_realstate_project_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Affiliate Supplier', 7, 'add_affiliatesupplieradd'),
(26, 'Can change Affiliate Supplier', 7, 'change_affiliatesupplieradd'),
(27, 'Can delete Affiliate Supplier', 7, 'delete_affiliatesupplieradd'),
(28, 'Can view Affiliate Supplier', 7, 'view_affiliatesupplieradd'),
(29, 'Can add Certified', 8, 'add_certifiedadd'),
(30, 'Can change Certified', 8, 'change_certifiedadd'),
(31, 'Can delete Certified', 8, 'delete_certifiedadd'),
(32, 'Can view Certified', 8, 'view_certifiedadd'),
(33, 'Can add Message', 9, 'add_chairmessage'),
(34, 'Can change Message', 9, 'change_chairmessage'),
(35, 'Can delete Message', 9, 'delete_chairmessage'),
(36, 'Can view Message', 9, 'view_chairmessage'),
(37, 'Can add Company', 10, 'add_companyprofile'),
(38, 'Can change Company', 10, 'change_companyprofile'),
(39, 'Can delete Company', 10, 'delete_companyprofile'),
(40, 'Can view Company', 10, 'view_companyprofile'),
(41, 'Can add Contact Message', 11, 'add_contactmessage'),
(42, 'Can change Contact Message', 11, 'change_contactmessage'),
(43, 'Can delete Contact Message', 11, 'delete_contactmessage'),
(44, 'Can view Contact Message', 11, 'view_contactmessage'),
(45, 'Can add Event Gallery', 12, 'add_eventgallery'),
(46, 'Can change Event Gallery', 12, 'change_eventgallery'),
(47, 'Can delete Event Gallery', 12, 'delete_eventgallery'),
(48, 'Can view Event Gallery', 12, 'view_eventgallery'),
(49, 'Can add Faq', 13, 'add_faq'),
(50, 'Can change Faq', 13, 'change_faq'),
(51, 'Can delete Faq', 13, 'delete_faq'),
(52, 'Can view Faq', 13, 'view_faq'),
(53, 'Can add HotNumber', 14, 'add_hotnumber'),
(54, 'Can change HotNumber', 14, 'change_hotnumber'),
(55, 'Can delete HotNumber', 14, 'delete_hotnumber'),
(56, 'Can view HotNumber', 14, 'view_hotnumber'),
(57, 'Can add Privacy', 15, 'add_privacypolicy'),
(58, 'Can change Privacy', 15, 'change_privacypolicy'),
(59, 'Can delete Privacy', 15, 'delete_privacypolicy'),
(60, 'Can view Privacy', 15, 'view_privacypolicy'),
(61, 'Can add Quality', 16, 'add_qualityadd'),
(62, 'Can change Quality', 16, 'change_qualityadd'),
(63, 'Can delete Quality', 16, 'delete_qualityadd'),
(64, 'Can view Quality', 16, 'view_qualityadd'),
(65, 'Can add Slider', 17, 'add_sliderbanner'),
(66, 'Can change Slider', 17, 'change_sliderbanner'),
(67, 'Can delete Slider', 17, 'delete_sliderbanner'),
(68, 'Can view Slider', 17, 'view_sliderbanner'),
(69, 'Can add Team Member', 18, 'add_teammemberinfo'),
(70, 'Can change Team Member', 18, 'change_teammemberinfo'),
(71, 'Can delete Team Member', 18, 'delete_teammemberinfo'),
(72, 'Can view Team Member', 18, 'view_teammemberinfo'),
(73, 'Can add Terms', 19, 'add_termsconditions'),
(74, 'Can change Terms', 19, 'change_termsconditions'),
(75, 'Can delete Terms', 19, 'delete_termsconditions'),
(76, 'Can view Terms', 19, 'view_termsconditions'),
(77, 'Can add Testimonial', 20, 'add_testimonialadd'),
(78, 'Can change Testimonial', 20, 'change_testimonialadd'),
(79, 'Can delete Testimonial', 20, 'delete_testimonialadd'),
(80, 'Can view Testimonial', 20, 'view_testimonialadd'),
(81, 'Can add Testimonial', 21, 'add_testimonialvideo'),
(82, 'Can change Testimonial', 21, 'change_testimonialvideo'),
(83, 'Can delete Testimonial', 21, 'delete_testimonialvideo'),
(84, 'Can view Testimonial', 21, 'view_testimonialvideo'),
(85, 'Can add sister  concern', 22, 'add_sisternconcernentry'),
(86, 'Can change sister  concern', 22, 'change_sisternconcernentry'),
(87, 'Can delete sister  concern', 22, 'delete_sisternconcernentry'),
(88, 'Can view sister  concern', 22, 'view_sisternconcernentry'),
(89, 'Can add Sistern Concern', 23, 'add_sisternconcerndetails'),
(90, 'Can change Sistern Concern', 23, 'change_sisternconcerndetails'),
(91, 'Can delete Sistern Concern', 23, 'delete_sisternconcerndetails'),
(92, 'Can view Sistern Concern', 23, 'view_sisternconcerndetails'),
(93, 'Can add service', 24, 'add_servicedetails'),
(94, 'Can change service', 24, 'change_servicedetails'),
(95, 'Can delete service', 24, 'delete_servicedetails'),
(96, 'Can view service', 24, 'view_servicedetails'),
(97, 'Can add service', 25, 'add_serviceentry'),
(98, 'Can change service', 25, 'change_serviceentry'),
(99, 'Can delete service', 25, 'delete_serviceentry'),
(100, 'Can view service', 25, 'view_serviceentry'),
(101, 'Can add User', 26, 'add_userregistrations'),
(102, 'Can change User', 26, 'change_userregistrations'),
(103, 'Can delete User', 26, 'delete_userregistrations'),
(104, 'Can view User', 26, 'view_userregistrations'),
(105, 'Can add Property', 27, 'add_propertyownership'),
(106, 'Can change Property', 27, 'change_propertyownership'),
(107, 'Can delete Property', 27, 'delete_propertyownership'),
(108, 'Can view Property', 27, 'view_propertyownership'),
(109, 'Can add Property', 28, 'add_propertyphoto'),
(110, 'Can change Property', 28, 'change_propertyphoto'),
(111, 'Can delete Property', 28, 'delete_propertyphoto'),
(112, 'Can view Property', 28, 'view_propertyphoto'),
(113, 'Can add Property', 29, 'add_propertyvideo'),
(114, 'Can change Property', 29, 'change_propertyvideo'),
(115, 'Can delete Property', 29, 'delete_propertyvideo'),
(116, 'Can view Property', 29, 'view_propertyvideo'),
(117, 'Can add Facility', 30, 'add_facility'),
(118, 'Can change Facility', 30, 'change_facility'),
(119, 'Can delete Facility', 30, 'delete_facility'),
(120, 'Can view Facility', 30, 'view_facility'),
(121, 'Can add Property', 31, 'add_propertyfacility'),
(122, 'Can change Property', 31, 'change_propertyfacility'),
(123, 'Can delete Property', 31, 'delete_propertyfacility'),
(124, 'Can view Property', 31, 'view_propertyfacility'),
(125, 'Can add Amenity', 32, 'add_amenity'),
(126, 'Can change Amenity', 32, 'change_amenity'),
(127, 'Can delete Amenity', 32, 'delete_amenity'),
(128, 'Can view Amenity', 32, 'view_amenity'),
(129, 'Can add Property', 33, 'add_propertyamenity'),
(130, 'Can change Property', 33, 'change_propertyamenity'),
(131, 'Can delete Property', 33, 'delete_propertyamenity'),
(132, 'Can view Property', 33, 'view_propertyamenity'),
(133, 'Can add PlotLand Facility', 34, 'add_landfacilityentry'),
(134, 'Can change PlotLand Facility', 34, 'change_landfacilityentry'),
(135, 'Can delete PlotLand Facility', 34, 'delete_landfacilityentry'),
(136, 'Can view PlotLand Facility', 34, 'view_landfacilityentry'),
(137, 'Can add PlotLand', 35, 'add_plotlandfacility'),
(138, 'Can change PlotLand', 35, 'change_plotlandfacility'),
(139, 'Can delete PlotLand', 35, 'delete_plotlandfacility'),
(140, 'Can view PlotLand', 35, 'view_plotlandfacility'),
(141, 'Can add Location', 36, 'add_locationadd'),
(142, 'Can change Location', 36, 'change_locationadd'),
(143, 'Can delete Location', 36, 'delete_locationadd'),
(144, 'Can view Location', 36, 'view_locationadd'),
(145, 'Can add Project', 37, 'add_projectadd'),
(146, 'Can change Project', 37, 'change_projectadd'),
(147, 'Can delete Project', 37, 'delete_projectadd'),
(148, 'Can view Project', 37, 'view_projectadd'),
(149, 'Can add Project', 38, 'add_projectplotland'),
(150, 'Can change Project', 38, 'change_projectplotland'),
(151, 'Can delete Project', 38, 'delete_projectplotland'),
(152, 'Can view Project', 38, 'view_projectplotland'),
(153, 'Can add Construction', 39, 'add_constructionstatus'),
(154, 'Can change Construction', 39, 'change_constructionstatus'),
(155, 'Can delete Construction', 39, 'delete_constructionstatus'),
(156, 'Can view Construction', 39, 'view_constructionstatus'),
(157, 'Can add Phase', 40, 'add_phaseadd'),
(158, 'Can change Phase', 40, 'change_phaseadd'),
(159, 'Can delete Phase', 40, 'delete_phaseadd'),
(160, 'Can view Phase', 40, 'view_phaseadd'),
(161, 'Can add PlotLand', 41, 'add_plotlandentry'),
(162, 'Can change PlotLand', 41, 'change_plotlandentry'),
(163, 'Can delete PlotLand', 41, 'delete_plotlandentry'),
(164, 'Can view PlotLand', 41, 'view_plotlandentry'),
(165, 'Can add Property', 42, 'add_propertytype'),
(166, 'Can change Property', 42, 'change_propertytype'),
(167, 'Can delete Property', 42, 'delete_propertytype'),
(168, 'Can view Property', 42, 'view_propertytype'),
(169, 'Can add Sales', 43, 'add_salesstatus'),
(170, 'Can change Sales', 43, 'change_salesstatus'),
(171, 'Can delete Sales', 43, 'delete_salesstatus'),
(172, 'Can view Sales', 43, 'view_salesstatus'),
(173, 'Can add PlotLand', 44, 'add_plotlandstatus'),
(174, 'Can change PlotLand', 44, 'change_plotlandstatus'),
(175, 'Can delete PlotLand', 44, 'delete_plotlandstatus'),
(176, 'Can view PlotLand', 44, 'view_plotlandstatus'),
(177, 'Can add Property', 45, 'add_propertyentry'),
(178, 'Can change Property', 45, 'change_propertyentry'),
(179, 'Can delete Property', 45, 'delete_propertyentry'),
(180, 'Can view Property', 45, 'view_propertyentry'),
(181, 'Can add Measurement', 46, 'add_measurementscale'),
(182, 'Can change Measurement', 46, 'change_measurementscale'),
(183, 'Can delete Measurement', 46, 'delete_measurementscale'),
(184, 'Can view Measurement', 46, 'view_measurementscale');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(2, 'pbkdf2_sha256$260000$DHm9bPP4WsmDRBdD7cU3fM$JUbmw+K2tRL4G0YyduTny1KDYKTldPdevu9+1a+uVbM=', '2023-03-04 13:18:25.641648', 1, 'user', 'Jahurul', 'Islam', 'ilovejahurul@gmail.com', 1, 1, '2023-02-28 06:16:53.000000'),
(3, 'pbkdf2_sha256$390000$N9XhzfK41AkhWQbv7irBII$NdhcOsFqNU2fZQeRNoM0AJYgdkzvIYFhmMdI8uVH820=', '2023-05-24 10:20:08.520803', 1, 'jahir', '', '', '', 1, 1, '2023-05-24 10:15:11.083038');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(55, '2023-02-28 06:17:48.887614', '2', 'user', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\"]}}]', 4, 2),
(56, '2023-02-28 10:23:40.118758', '2', 'Mohammad Ismail', 2, '[{\"changed\": {\"fields\": [\"Date of birth\"]}}]', 26, 2),
(57, '2023-03-01 10:48:23.448076', '1', 'ChairMessage object (1)', 2, '[{\"changed\": {\"fields\": [\"Message\"]}}]', 9, 2),
(58, '2023-03-01 13:57:35.726010', '1', 'Jahurul Islam', 2, '[{\"changed\": {\"fields\": [\"User type\"]}}]', 26, 2),
(59, '2023-03-01 13:57:47.680580', '2', 'Mohammad Ismail', 2, '[{\"changed\": {\"fields\": [\"User type\"]}}]', 26, 2),
(60, '2023-03-04 12:53:33.975276', '2', 'Mohammad Ismail', 2, '[{\"changed\": {\"fields\": [\"User type\", \"Address\"]}}]', 26, 2),
(61, '2023-03-04 12:59:28.858002', '3', '01322301174', 1, '[{\"added\": {}}]', 4, 2),
(62, '2023-03-04 13:09:08.315130', '3', 'Sakib', 1, '[{\"added\": {}}]', 26, 2),
(63, '2023-03-04 13:12:02.733553', '3', '01322301174', 3, '', 4, 2),
(64, '2023-05-24 10:21:03.641935', '2', 'Md. Eshaq Ali', 2, '[{\"changed\": {\"fields\": [\"Member name\", \"Member image\", \"Member disignation\", \"Facebook link\", \"Twitter link\", \"Instragram link\"]}}]', 18, 3),
(65, '2023-05-24 10:21:31.964215', '2', 'Md. Eshaq Ali', 2, '[{\"changed\": {\"fields\": [\"Member image\"]}}]', 18, 3),
(66, '2023-05-24 10:21:57.790195', '1', 'Full Name', 2, '[{\"changed\": {\"fields\": [\"Member image\", \"Member disignation\", \"Facebook link\", \"Twitter link\", \"Instragram link\"]}}]', 18, 3);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(32, 'property', 'amenity'),
(39, 'property', 'constructionstatus'),
(30, 'property', 'facility'),
(34, 'property', 'landfacilityentry'),
(36, 'property', 'locationadd'),
(46, 'property', 'measurementscale'),
(40, 'property', 'phaseadd'),
(41, 'property', 'plotlandentry'),
(35, 'property', 'plotlandfacility'),
(44, 'property', 'plotlandstatus'),
(37, 'property', 'projectadd'),
(38, 'property', 'projectplotland'),
(33, 'property', 'propertyamenity'),
(45, 'property', 'propertyentry'),
(31, 'property', 'propertyfacility'),
(27, 'property', 'propertyownership'),
(28, 'property', 'propertyphoto'),
(42, 'property', 'propertytype'),
(29, 'property', 'propertyvideo'),
(43, 'property', 'salesstatus'),
(7, 'realstateapp', 'affiliatesupplieradd'),
(8, 'realstateapp', 'certifiedadd'),
(9, 'realstateapp', 'chairmessage'),
(10, 'realstateapp', 'companyprofile'),
(11, 'realstateapp', 'contactmessage'),
(12, 'realstateapp', 'eventgallery'),
(13, 'realstateapp', 'faq'),
(14, 'realstateapp', 'hotnumber'),
(15, 'realstateapp', 'privacypolicy'),
(16, 'realstateapp', 'qualityadd'),
(24, 'realstateapp', 'servicedetails'),
(25, 'realstateapp', 'serviceentry'),
(23, 'realstateapp', 'sisternconcerndetails'),
(22, 'realstateapp', 'sisternconcernentry'),
(17, 'realstateapp', 'sliderbanner'),
(18, 'realstateapp', 'teammemberinfo'),
(19, 'realstateapp', 'termsconditions'),
(20, 'realstateapp', 'testimonialadd'),
(21, 'realstateapp', 'testimonialvideo'),
(26, 'realstateapp', 'userregistrations'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-02-26 10:22:42.933032'),
(2, 'auth', '0001_initial', '2023-02-26 10:22:45.144295'),
(3, 'admin', '0001_initial', '2023-02-26 10:22:47.237893'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-02-26 10:22:47.568048'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-02-26 10:22:47.597101'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-02-26 10:22:47.867584'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-02-26 10:22:48.104829'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-02-26 10:22:48.170285'),
(9, 'auth', '0004_alter_user_username_opts', '2023-02-26 10:22:48.201705'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-02-26 10:22:48.390910'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-02-26 10:22:48.400911'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-02-26 10:22:48.410920'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-02-26 10:22:48.447981'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-02-26 10:22:48.481094'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-02-26 10:22:48.525360'),
(16, 'auth', '0011_update_proxy_permissions', '2023-02-26 10:22:48.545363'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-02-26 10:22:48.576265'),
(18, 'sessions', '0001_initial', '2023-02-26 10:22:49.084905'),
(19, 'realstateapp', '0001_initial', '2023-02-26 10:35:13.666164'),
(20, 'property', '0001_initial', '2023-02-26 10:35:16.975382'),
(21, 'realstateapp', '0002_auto_20230226_1638', '2023-02-26 10:38:56.507678'),
(22, 'property', '0002_auto_20230226_2304', '2023-02-26 17:04:21.035545'),
(23, 'realstateapp', '0003_auto_20230227_0038', '2023-02-26 18:38:48.993182'),
(24, 'realstateapp', '0004_auto_20230227_1059', '2023-02-27 04:59:45.012779'),
(25, 'realstateapp', '0005_auto_20230227_1102', '2023-02-27 05:02:30.858081'),
(26, 'realstateapp', '0006_auto_20230227_1141', '2023-02-27 05:41:31.092923'),
(27, 'realstateapp', '0007_auto_20230227_1413', '2023-02-27 08:13:55.000459'),
(28, 'realstateapp', '0008_auto_20230227_1534', '2023-02-27 09:34:49.807400'),
(29, 'realstateapp', '0009_auto_20230227_1544', '2023-02-27 09:44:55.889204'),
(30, 'realstateapp', '0010_auto_20230227_1546', '2023-02-27 09:46:29.124499'),
(31, 'realstateapp', '0011_auto_20230228_1155', '2023-02-28 05:55:18.362852'),
(32, 'property', '0003_auto_20230228_0734', '2023-02-28 07:47:56.264515'),
(33, 'realstateapp', '0012_auto_20230228_0734', '2023-02-28 07:47:56.896774'),
(34, 'realstateapp', '0013_alter_userregistrations_date_of_birth', '2023-02-28 09:29:31.723095'),
(35, 'realstateapp', '0014_userregistrations_user_type', '2023-03-01 13:42:34.495067'),
(36, 'property', '0004_auto_20230313_1235', '2023-03-13 12:35:41.223570');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('014jw88odejxzshp21m7gqlrmhrprvht', 'eyJ1c2VyaWQiOmZhbHNlfQ:1q1lmG:ouStK42olrvUe2k8nTPFxRksX_elWvCqr_Ob4IP7I2E', '2023-06-07 10:31:32.358012'),
('1gduex65b3zxoompkoabifeal86npbvs', '.eJxVjksOgzAMRO_iNUL5kKB02X3PgJzYKfRDKgLqourdm1RsWHrem5E_sGVehmfy04PhBEL2VjgreuOggRfm_E4LFSCV7kpS7ancsoEBt3Uc_vWagIJD5jHcea6AbjhfUxvSvC6Tb6vS7jS3l0T8OO_uYWDEPJY29kRKOa2Jg4qdMUYqISKVL62w2gd2Bn3nHaGMyJpdkFEaNoqsjbqH7w_LfUiE:1pXJwQ:KqX51oseRxdja3-lBDdmPH01LBgokPmteQNHMGcppso', '2023-03-15 10:44:10.801125'),
('28vnfdt603pxh9917g5qq9yb2lavlxtp', 'eyJ1c2VyX21vYmlsZSI6IjAxMzIyMzAxMTc0IiwicGFzc3dvcmQiOiJzYWtpYjEyMyIsInVzZXJpZCI6M30:1pd44T:gKhq1TH81QIQn-mGhUovwi4mvU6eRu0ea-5kD-MTlSs', '2023-03-31 07:00:13.798196'),
('3lkm9z7n5x8t4pptua7vyoetpui1ghwy', 'eyJ1c2VyX21vYmlsZSI6IjAxNzYwOTYwNzU5IiwicGFzc3dvcmQiOiIxMjM0IiwidXNlcmlkIjpmYWxzZX0:1qryrZ:wZvtLW-7ze0IqXewShrEJ0f7utp4QbUqVSKyjmXTjts', '2023-10-29 11:00:49.625240'),
('6qfb4m5mo6o93dt9oqowl9p9k73i2zak', 'eyJ1c2VyX21vYmlsZSI6IjAxMzIyMzAxMTc0IiwicGFzc3dvcmQiOiJzYWtpYjEyMyIsInVzZXJpZCI6M30:1pbgXd:FRJ-J7MkatERcTRiq6f34RRH4chgSG91XgTP8hhLkrA', '2023-03-27 11:40:37.009136'),
('6thq87o7wbu96mtd2r2g3ixzouphrwwr', 'eyJ1c2VyX21vYmlsZSI6IjAxNzYwOTYwNzU5IiwicGFzc3dvcmQiOiIxMjM0IiwidXNlcmlkIjoxfQ:1pblNF:ImNy7c_GTv-3DxjzHI74-NFcg8NeC4fo9-vlD0lqLjU', '2023-03-27 16:50:13.667362'),
('8tildffnpkt8dqcvw4k1ka8fh4yvoyur', 'eyJ1c2VyX21vYmlsZSI6IjAxMzAzMTAxODk2IiwicGFzc3dvcmQiOiJzdGkxMjMiLCJ1c2VyaWQiOjJ9:1pWwKp:rSzXdUcwVA71RIxzITsK5bVVHDByakqf8uwRy3QhK4U', '2023-03-14 09:31:47.361105'),
('c01a8c2jr4f8zcz0x0ulyyexpd2jbn40', 'eyJ1c2VyX21vYmlsZSI6IjAxMzIyMzAxMTc0IiwicGFzc3dvcmQiOiJzYWtpYjEyMyIsInVzZXJpZCI6M30:1pYhvZ:yxUlJdXJUEdTjlhMOTskXn2kiqMGKHlOGRjq6p0bIwA', '2023-03-19 06:33:01.491808'),
('dg8ssyyi3qvteeyxpshapqeenrtpfx7p', 'eyJ1c2VyX21vYmlsZSI6IjAxMzIyMzAxMTc0IiwicGFzc3dvcmQiOiJzYWtpYjEyMyIsInVzZXJpZCI6M30:1pZ4yP:oqc6GHmKVLwVHDcWFGGGxviJBp8oYaFks3zzhbouHxk', '2023-03-20 07:09:29.125999'),
('dh3s0tgk4grdql6xh5kdgzbamolidyyk', '.eJxVjksOgzAMRO_iNUL5kKCw7L5nQE7sFPohFQF1UfXuDYgNO2vmvZG_sGaeR4JOVvvZv5IfnwwdCNla4axojYMK3pjzJ80FBKl0U5Ie12Xod2fzQZ0zj-HB01bQHadbqkOalnn09YbUR5vrayJ-Xg72NDBgHoqNLZFSTmvioGJjjJFKiEjlNSus9oGdQd94RygjsmYXZJSGjSJro27h9wfZpEiE:1pWxUd:5WNDjJ8POX6dtJEG0686SYeZNKkKJHkh-0QVz7yZeeg', '2023-03-14 10:45:59.026707'),
('e6b6248bxft4jebvbrx0uvk9qr5ki8xf', '.eJyrViotTi2Kz81PysxJVbJSMjA0NjIyNjA0NDdW0lEqSCwuLs8vSsGQAGnKBAob1wIAd0sSaQ:1q7BaB:j3wwCgT0H4_lpSkyHzBt7pVzeSvsZBWmnEJRo_VSVSo', '2023-06-22 09:05:27.706535'),
('ehn1vh5t6ghee2dwp5pgut5fmjrty4rr', '.eJyrViotTi2Kz81PysxJVbJSMjA0NjIyNjA0NDdW0lEqSCwuLs8vSsGQAGnKBAqnJeYUp9YCAMXlFEE:1plQFq:0E9tVWD3wfGRRovGTKK4wooFDH02YYjDpV3VEdrItmE', '2023-04-23 08:18:30.775380'),
('fw4159n09y040pjvgsyf5dkhbegq724d', 'eyJ1c2VyX21vYmlsZSI6IjAxNzYwOTYwNzU5IiwicGFzc3dvcmQiOiIxMjM0IiwidXNlcmlkIjpmYWxzZX0:1pcoSX:BR-FffzvkRZ8hg-EVtCJAS-Sym3yUBB0-VpO3avZ6Lw', '2023-03-30 14:20:01.405806'),
('hvr0otzx89tdp4zcc8ax9pbpmkzyhk1v', '.eJyrViotTi2Kz81PysxJVbJSMjA0NjIyNjA0NDdW0lEqSCwuLs8vSsGQAGnKBAob1wIAd0sSaQ:1plQ5b:Lr8iloTsQK7NRpGKEbRnQ4v6TkV5qU7kpVaowWYfpfQ', '2023-04-23 08:07:55.152115'),
('ikwk5zlslgv7etb9k1uqyilbcwcuoadr', '.eJxVj0EOgjAQRe_C2pB2hpbUpXvPQKadqSBKDYW4MN7dYljodt7_L39eVUfr0ndrlrkbuDpWUB1-b57CKNMG-ErTJdUhTcs8-HqL1DvN9Tmx3E579k_QU-5Lm1pmAIfIEiA2xhgNSkVWzlpl0QdxhnzjHZOOJCgu6KiNGGBrI7ZF-tXdkx9uUoRKIwAqrdumsAfl_EzztjPTOHgNuDe2p_D9AXOKSkI:1pYRpA:WtZlD6VQpFmICtFnESjAb438DPsL-1nGY3ijVyIMc0Q', '2023-03-18 13:21:20.149875'),
('lc12cv2w2n0xnlko9cw6cb9g4nnhzrci', '.eJyrViotTi2Kz81PysxJVbJSMjA0NjIyNjA0NDdW0lEqSCwuLs8vSsGQAGnKBAob1wIAd0sSaQ:1qYp4b:HhnS4lGpNLe7Y8r4nHqzilsbqKaIPNMRBF3c9r4QiJo', '2023-09-06 14:43:05.899847'),
('o9r8yq310zypu9p706pt682vbkmkokro', '.eJxVjEEOwiAQAP_C2ZCyUASP3n0D2WVBqgaS0p6MfzckPeh1ZjJvEXDfSth7WsPC4iJAnH4ZYXymOgQ_sN6bjK1u60JyJPKwXd4ap9f1aP8GBXsZW0SyYAwo6xRHQ0yoQDltKHnIE0wcvTs7dhoZoqc866SMTp5iBjuLzxffRjfz:1pWtIk:pM6JTbSm7-glp7sVlGiw1SsEMGVAAmTelilGrBtmLdw', '2023-03-14 06:17:26.969673'),
('oxewtmhwcs5yuf9xdi5rh9u55rpd5dr9', '.eJxVjEEOwiAQRe_C2hAYZEpduu8ZyACDVA0kpV0Z765NutDtf-_9l_C0rcVvnRc_J3ERWpx-t0DxwXUH6U711mRsdV3mIHdFHrTLqSV-Xg_376BQL9-ao7WjcegUIEcgC0kREWgFzqFFMhlGRojaZggmsYEh6HAeMmlAIPH-AMtAN1g:1pWEPw:TIHyxaFL4a2MIupgRQXhSVXs772227KmwmPZ_Y_nBpI', '2023-03-12 10:38:08.271802'),
('t8itqa72a2vry1tn7x9liywpwzhezhjt', 'eyJ1c2VyX21vYmlsZSI6IjAxMzIyMzAxMTc0IiwicGFzc3dvcmQiOiJzYWtpYjEyMyIsInVzZXJpZCI6M30:1pgMuK:zrDKMRpd5ksYXD3rmcbaUa5iGrJFnbVmYI7jeYDLLQs', '2023-04-09 09:43:24.254058'),
('tf6begv2fvuzl1ly92ouqhprf5zlfs7c', 'eyJ1c2VyX21vYmlsZSI6IjAxNzYwOTYwNzU5IiwicGFzc3dvcmQiOiIxMjM0IiwidXNlcmlkIjpmYWxzZX0:1qN8Og:8etlmAk9FyNwipI4fKunntEDQxW-13BHxqzPDo5oFnk', '2023-08-05 08:55:30.157098'),
('xoba0r27r94hfaxs25f95itc1e6o90uq', 'eyJ1c2VyX21vYmlsZSI6IjAxNzYwOTYwNzU5IiwicGFzc3dvcmQiOiIxMjM0IiwidXNlcmlkIjoxfQ:1pcmtS:wSSJTOfa7APgVVUlZzq6zk_pV1LOF2mvejHJD8kBRtw', '2023-03-30 12:39:42.797572'),
('ykczzm3luang0x06v9kf6s4eka7zdwjn', '.eJxVj8sOwiAQRf-FtSE8CgSX7v2GZmAGW63FlDYujP8umC50O-fekzsv1sO2Dv1WaOlHZEem2OH3FiDeaG4ArzBfMo95Xpcx8BbhOy38nJGm0579EwxQhtoGh6iU1xopqtQZY6QSIqHw1gqrQyRvIHTBI8gEpMlHmaQho9DapF2VfnX3HMaJqlBIZ2tZOOMre0Apz7y0nVLpbk-3hxJMhd4fbHNKXg:1pbiEI:OPkpG6AIJh6BLPjkEjINLYb4gPyQt8mjqlCLYxuieF8', '2023-03-27 13:28:46.607078');

-- --------------------------------------------------------

--
-- Table structure for table `property_amenity`
--

CREATE TABLE `property_amenity` (
  `id` bigint NOT NULL,
  `amenity_name` varchar(300) NOT NULL,
  `amenity_icon` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_amenity`
--

INSERT INTO `property_amenity` (`id`, `amenity_name`, `amenity_icon`, `status`) VALUES
(1, 'fire fighting system', 'amenity_icon/fire-reque.png', 1),
(2, 'parking', 'amenity_icon/parking-icon.png', 1),
(3, 'community support', 'amenity_icon/community-support_KVgKqyO.png', 1),
(4, 'power sub-station', 'amenity_icon/power-station.png', 1),
(5, 'inter-communication', 'amenity_icon/telephone_Fo82Iaa.png', 1),
(6, 'Near University', 'amenity_icon/school.png', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_constructionstatus`
--

CREATE TABLE `property_constructionstatus` (
  `id` bigint NOT NULL,
  `construction_status` varchar(300) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_constructionstatus`
--

INSERT INTO `property_constructionstatus` (`id`, `construction_status`, `status`) VALUES
(1, 'Completed', 1),
(2, 'under construction', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_facility`
--

CREATE TABLE `property_facility` (
  `id` bigint NOT NULL,
  `facility_name` varchar(300) NOT NULL,
  `facility_icon` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_facility`
--

INSERT INTO `property_facility` (`id`, `facility_name`, `facility_icon`, `status`) VALUES
(1, 'Near School /Madrasah', 'facility_icon/school.png', 1),
(2, 'Near Play-Ground', 'facility_icon/play-ground.png', 1),
(3, 'Near Hospital', 'facility_icon/hospital.png', 1),
(4, 'Near metro rail', 'facility_icon/metro-rail.png', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_landfacilityentry`
--

CREATE TABLE `property_landfacilityentry` (
  `id` bigint NOT NULL,
  `land_facility_name` varchar(300) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `property_locationadd`
--

CREATE TABLE `property_locationadd` (
  `id` bigint NOT NULL,
  `location_name` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_locationadd`
--

INSERT INTO `property_locationadd` (`id`, `location_name`, `status`) VALUES
(1, 'Uttara', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_measurementscale`
--

CREATE TABLE `property_measurementscale` (
  `id` bigint NOT NULL,
  `measurement_scale` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_measurementscale`
--

INSERT INTO `property_measurementscale` (`id`, `measurement_scale`, `status`) VALUES
(1, 'Katha', 1),
(2, 'Bigha', 1),
(3, 'Accor', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_phaseadd`
--

CREATE TABLE `property_phaseadd` (
  `id` bigint NOT NULL,
  `phase_name` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_phaseadd`
--

INSERT INTO `property_phaseadd` (`id`, `phase_name`, `status`) VALUES
(1, 'Upcoming', 1),
(2, 'Ongoing', 1),
(3, 'Completed', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_plotlandentry`
--

CREATE TABLE `property_plotlandentry` (
  `id` bigint NOT NULL,
  `date` date DEFAULT NULL,
  `plotland_id` int DEFAULT NULL,
  `plot_land_image` varchar(100) NOT NULL,
  `land_size` int DEFAULT NULL,
  `block` varchar(1200) NOT NULL,
  `sector` int DEFAULT NULL,
  `road_no` int DEFAULT NULL,
  `plot_no` int DEFAULT NULL,
  `google_map_url` longtext,
  `address` longtext,
  `status` tinyint(1) NOT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `developer_name_id` bigint DEFAULT NULL,
  `measurement_scale_id` bigint DEFAULT NULL,
  `plot_land_status_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `property_plotlandfacility`
--

CREATE TABLE `property_plotlandfacility` (
  `id` bigint NOT NULL,
  `plotland_id` int DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `land_facility_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `property_plotlandstatus`
--

CREATE TABLE `property_plotlandstatus` (
  `id` bigint NOT NULL,
  `land_status_name` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_plotlandstatus`
--

INSERT INTO `property_plotlandstatus` (`id`, `land_status_name`, `status`) VALUES
(1, 'Ready', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_projectadd`
--

CREATE TABLE `property_projectadd` (
  `id` bigint NOT NULL,
  `project_name` varchar(300) NOT NULL,
  `project_logo` varchar(100) NOT NULL,
  `developer_name` varchar(200) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `total_apartment` int DEFAULT NULL,
  `land_size` varchar(300) DEFAULT NULL,
  `total_units` int DEFAULT NULL,
  `lift` int DEFAULT NULL,
  `stairs` int DEFAULT NULL,
  `face` varchar(200) DEFAULT NULL,
  `plot_no` varchar(200) DEFAULT NULL,
  `block_no` varchar(200) DEFAULT NULL,
  `road_size` varchar(200) DEFAULT NULL,
  `parking_ability` varchar(200) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `project_type_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_projectadd`
--

INSERT INTO `property_projectadd` (`id`, `project_name`, `project_logo`, `developer_name`, `address`, `total_apartment`, `land_size`, `total_units`, `lift`, `stairs`, `face`, `plot_no`, `block_no`, `road_size`, `parking_ability`, `status`, `created_by_id`, `project_type_id`) VALUES
(1, 'Royal Tower', '', 'STI BUILDERS LTD', 'Beside Uttara Sector-17, neer Metro Rail, Bes', 1, '18 katha', 78, 2, 2, 'south', 'G-2', '', '60 feet and 30 feet', 'YES', 1, 3, 1),
(2, 'Lake Drive paradise', '', 'STI BUILDERS LTD', 'Uttara Sector-17, Beside Metro Rail 2nd station', 1, '9.22', 33, 2, 1, 'South and lake face', '', '', '60 feet and 30 feet', 'YES', 1, 3, 1),
(3, 'SOUTH PALACE', 'logo/WhatsApp Image 2023-02-27 at 12.59.38 PM.jpeg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '12', 44, 2, 1, 'South', '08', 'A', '30 feet X 20 feet', 'Yes', 1, 3, 1),
(4, 'TEXTILE PALCE', 'logo/WhatsApp Image 2023-02-26 at 4.28.59 PM (1).jpeg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '9.5', 33, 2, 1, 'South', '9', 'A', '30 feet and 20 feet', 'Yes', 1, 3, 1),
(5, 'STI ORCHID', 'logo/WhatsApp Image 2023-03-05 at 3.16.13 PM.jpeg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '15', 66, 2, 2, 'South', '1', 'A', '30 feet x 30feet', 'Yes', 1, 3, 1),
(6, 'STI ROSE GARDEN', 'logo/WhatsApp Image 2023-03-05 at 3.23.04 PM.jpeg', 'STI BUILDERS LTD', 'Uttara Sector-15,neer Metro Rail 1ST STATION', 1, '10', 44, 2, 1, 'NORTH', '6', 'A', '30 feet X 20 feet', 'Yes', 1, 3, 1),
(7, 'S.I. PALACE', 'logo/WhatsApp Image 2023-03-05 at 3.27.18 PM.jpeg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 3, '29.09', 144, 6, 4, 'South', '', '', '30 feet', 'Yes', 1, 3, 1),
(8, 'BANDON-4', 'logo/B-4.jpg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '12', 36, 2, 1, 'South', '', '', '30 feet and 20 feet', 'Yes', 1, 3, 1),
(9, 'BANDON-6', 'logo/07-3.jpg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '10', 45, 2, 1, 'NORTH', '', '', '300 feet and 20 feet', 'Yes', 1, 3, 1),
(10, 'BANDON-3', 'logo/3.jpg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '10', 36, 2, 1, 'South', '', '', '30 feet', 'Yes', 1, 3, 1),
(11, 'STI METROY CITY', 'logo/WhatsApp Image 2023-03-05 at 4.28.01 PM.jpeg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 9, '132', 400, 18, 10, 'South', '', '', '30 feet X 20 feet', 'Yes', 1, 3, 1),
(12, 'COMPLEX -1', 'logo/apartment-building-14-01.jpg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '10', 36, 2, 2, 'SOUTH', '1', '', '30 feet and 20 feet', 'YES', 1, 3, 1),
(13, 'COMPLEX -2', 'logo/392de73c003ee682abc4faedc14f6449.jpg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '10', 44, 2, 1, 'SOUTH', '6', '', '30 feet and 20 feet', 'YES', 1, 3, 3),
(14, 'COMPLEX -3', 'logo/images (2).jpeg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '10', 44, 2, 1, 'SOUTH', '', '', '30 feet and 20 feet', 'YES', 1, 3, 4),
(15, 'BANDON -1', 'logo/images (3).jpeg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '6', 18, 1, 1, 'SOUTH', '', '', '30 feet and 20 feet', 'YES', 1, 3, 4),
(16, 'BANDON -2', 'logo/images.jpeg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '6.15', 18, 1, 1, 'SOUTH', '', '', '30 feet and 20 feet', 'YES', 1, 3, 4),
(17, 'BANDON -5', 'logo/vcxvxcbvbv-1.jpg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '5', 18, 1, 1, 'SOUTH', '', '', '30 feet and 20 feet', 'YES', 1, 3, 3),
(18, 'APON NIBAS', 'logo/popular3.jpg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '10.5', 44, 2, 1, 'SOUTH', '', '', '30 feet ', '', 1, 3, 4),
(19, 'STAR VIEW', 'logo/modern-building-23979479.jpg', 'STI BUILDERS LTD', 'Uttara Sector-15, Beside Metro Rail 1ST STATION', 1, '8.5', 33, 2, 1, 'SOUTH', '', '', '30 feet and 20 feet', '', 1, 3, 4);

-- --------------------------------------------------------

--
-- Table structure for table `property_projectplotland`
--

CREATE TABLE `property_projectplotland` (
  `id` bigint NOT NULL,
  `developer_name` varchar(200) DEFAULT NULL,
  `block` varchar(200) DEFAULT NULL,
  `sector` int DEFAULT NULL,
  `road_no` int DEFAULT NULL,
  `plot_no` int DEFAULT NULL,
  `land_size` int DEFAULT NULL,
  `size_unit` varchar(200) DEFAULT NULL,
  `plot_land_image` varchar(100) NOT NULL,
  `address` varchar(200) DEFAULT NULL,
  `map_url` longtext,
  `status` tinyint(1) NOT NULL,
  `created_by_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_projectplotland`
--

INSERT INTO `property_projectplotland` (`id`, `developer_name`, `block`, `sector`, `road_no`, `plot_no`, `land_size`, `size_unit`, `plot_land_image`, `address`, `map_url`, `status`, `created_by_id`) VALUES
(1, 'nandan Kanan construction ltd', 'block -c', 11, 15, 33, 50, 'acors', '', 'H-18, R-15, Sec-10, Uttara, Dhaka', '', 1, 1),
(2, 'nandan Kanan construction ltd', 'block -A', 15, 5, 35, 10, 'acors', 'plot_land_image/jahir.jpg', 'uttara', '', 1, 1),
(3, 'AK', 'block -A', 5, 17, 8, 45, 'acors', 'plot_land/plot_land_image/Land-Sharing.png', 'fdfsd', '', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_propertyamenity`
--

CREATE TABLE `property_propertyamenity` (
  `id` bigint NOT NULL,
  `property_id` int DEFAULT NULL,
  `amenity_icon` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `amenity_name_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_propertyamenity`
--

INSERT INTO `property_propertyamenity` (`id`, `property_id`, `amenity_icon`, `status`, `amenity_name_id`) VALUES
(1, 202303051, '', 1, 1),
(2, 202303051, '', 1, 2),
(3, 202303051, '', 1, 3),
(4, 202303051, '', 1, 4),
(5, 202303051, '', 1, 5),
(6, 202303051, '', 1, 6),
(7, 202302261, '', 1, 1),
(8, 202302261, '', 1, 2),
(9, 202302261, '', 1, 3),
(10, 202302261, '', 1, 4),
(11, 202302261, '', 1, 5),
(12, 202302261, '', 1, 6),
(13, 202303052, '', 1, 1),
(14, 202303052, '', 1, 2),
(15, 202303052, '', 1, 3),
(16, 202303052, '', 1, 4),
(17, 202303052, '', 1, 5),
(18, 202303052, '', 1, 6),
(19, 202303053, '', 1, 1),
(20, 202303053, '', 1, 3),
(21, 202303053, '', 1, 4),
(22, 202303053, '', 1, 5),
(23, 202303053, '', 1, 6),
(24, 202303054, '', 1, 1),
(25, 202303054, '', 1, 2),
(26, 202303054, '', 1, 3),
(27, 202303054, '', 1, 4),
(28, 202303054, '', 1, 5),
(29, 202303054, '', 1, 6),
(30, 202303055, '', 1, 1),
(31, 202303055, '', 1, 2),
(32, 202303055, '', 1, 3),
(33, 202303055, '', 1, 4),
(34, 202303055, '', 1, 5),
(35, 202303055, '', 1, 6),
(36, 202303056, '', 1, 1),
(37, 202303056, '', 1, 2),
(38, 202303056, '', 1, 3),
(39, 202303056, '', 1, 4),
(40, 202303056, '', 1, 5),
(41, 202303056, '', 1, 6),
(42, 202303132, '', 1, 1),
(43, 202303132, '', 1, 2),
(44, 202303132, '', 1, 3),
(45, 202303132, '', 1, 4),
(46, 202303132, '', 1, 5),
(47, 202303131, '', 1, 1),
(48, 202303131, '', 1, 2),
(49, 202303131, '', 1, 4),
(50, 202303131, '', 1, 5),
(51, 202303131, '', 1, 6),
(52, 202303133, '', 1, 1),
(53, 202303133, '', 1, 2),
(54, 202303133, '', 1, 3),
(55, 202303133, '', 1, 4),
(56, 202303133, '', 1, 5),
(57, 202303133, '', 1, 6),
(58, 202303134, '', 1, 1),
(59, 202303134, '', 1, 2),
(60, 202303134, '', 1, 3),
(61, 202303134, '', 1, 4),
(62, 202303134, '', 1, 5),
(63, 202303134, '', 1, 6),
(64, 202303135, '', 1, 1),
(65, 202303135, '', 1, 2),
(66, 202303135, '', 1, 3),
(67, 202303135, '', 1, 4),
(68, 202303135, '', 1, 5),
(69, 202303135, '', 1, 6),
(70, 202303136, '', 1, 1),
(71, 202303136, '', 1, 2),
(72, 202303136, '', 1, 3),
(73, 202303136, '', 1, 4),
(74, 202303136, '', 1, 5),
(75, 202303136, '', 1, 6),
(76, 202303137, '', 1, 1),
(77, 202303137, '', 1, 2),
(78, 202303137, '', 1, 3),
(79, 202303137, '', 1, 4),
(80, 202303137, '', 1, 5),
(81, 202303137, '', 1, 6),
(82, 202303138, '', 1, 1),
(83, 202303138, '', 1, 2),
(84, 202303138, '', 1, 3),
(85, 202303138, '', 1, 4),
(86, 202303138, '', 1, 5),
(87, 202303138, '', 1, 6),
(88, 202303139, '', 1, 1),
(89, 202303139, '', 1, 2),
(90, 202303139, '', 1, 4),
(91, 202303139, '', 1, 5),
(92, 202303139, '', 1, 6),
(93, 202303140, '', 1, 1),
(94, 202303140, '', 1, 2),
(95, 202303140, '', 1, 3),
(96, 202303140, '', 1, 4),
(97, 202303140, '', 1, 5),
(98, 202303140, '', 1, 6),
(99, 202303141, '', 1, 1),
(100, 202303141, '', 1, 2),
(101, 202303141, '', 1, 4),
(102, 202303141, '', 1, 5),
(103, 202303141, '', 1, 6);

-- --------------------------------------------------------

--
-- Table structure for table `property_propertyentry`
--

CREATE TABLE `property_propertyentry` (
  `id` bigint NOT NULL,
  `date` date DEFAULT NULL,
  `property_id` int DEFAULT NULL,
  `property_catagory` varchar(2) NOT NULL,
  `property_name` varchar(1200) NOT NULL,
  `selling_price` varchar(1500) NOT NULL,
  `property_area` varchar(500) NOT NULL,
  `brochure` varchar(100) DEFAULT NULL,
  `flor_plan` varchar(100) DEFAULT NULL,
  `bed` varchar(100) DEFAULT NULL,
  `bath` varchar(100) DEFAULT NULL,
  `number_of_belcony` varchar(200) NOT NULL,
  `daining_space` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `flat_apartment_no` varchar(200) NOT NULL,
  `kitchen_space` varchar(200) NOT NULL,
  `property_image` varchar(100) DEFAULT NULL,
  `property_banner` varchar(100) DEFAULT NULL,
  `location_map` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `choose_phase` varchar(500) NOT NULL,
  `construction_status` varchar(500) NOT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `location` varchar(500) NOT NULL,
  `project_name` varchar(500) NOT NULL,
  `property_type` varchar(500) NOT NULL,
  `sales_type` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_propertyentry`
--

INSERT INTO `property_propertyentry` (`id`, `date`, `property_id`, `property_catagory`, `property_name`, `selling_price`, `property_area`, `brochure`, `flor_plan`, `bed`, `bath`, `number_of_belcony`, `daining_space`, `address`, `flat_apartment_no`, `kitchen_space`, `property_image`, `property_banner`, `location_map`, `status`, `choose_phase`, `construction_status`, `created_by_id`, `location`, `project_name`, `property_type`, `sales_type`) VALUES
(1, '2023-02-26', 202302261, '2', 'ROYAL TOWER', '59,00,000', '1850', 'brochure/BDRAILWAY_TICKET202302131645358430178.pdf', 'flor_plan/property.png', '3', '3', '3', '3.21M X 4.06M', '                   Beside sector 17,Uttara,Near Metro Rail 2nd &3rd station,Dhaka', '1', '1.95M X 2.10M', 'property_image/WhatsApp Image 2023-02-26 at 5.42.05 PM (1).jpeg', 'property_banner/WhatsApp Image 2023-03-01 at 11.00.04 AM.jpeg', '                                        ', 1, 'Ongoing', 'Completed', 1, 'Uttara', 'Royal Tower', 'Residential', 'Avaiable'),
(2, '2023-03-05', 202303051, '2', 'STI LAKE DRIVE PAEADISE', '57,000,00', '1850', '', '', '4', '4', '4', '32.4 x 12.4', '           Beside sector 17,Uttara,Near Metro Rail 2nd &3rd station,Dhaka', '2', '9 x8', 'property_image/WhatsApp Image 2023-03-11 at 9.27.52 PM.jpeg', 'property_banner/WhatsApp Image 2023-03-01 at 11.00.04 AM (3).jpeg', '                      ', 1, 'Ongoing', 'Completed', 1, 'Uttara', 'Lake Drive paradise', 'Residential', 'Avaiable'),
(3, '2023-03-05', 202303052, '2', 'TEXTILE  PALACE', '52,00,000', '1850', '', '', '3', '3', '3', '27.3 X 10.3', '         Beside sector 15,Uttara,Near Metro Rail  station,Dhaka', '9', '8X 12.8', 'property_image/WhatsApp Image 2023-02-26 at 4.28.59 PM (1).jpeg', 'property_banner/WhatsApp Image 2023-03-01 at 11.00.04 AM_HvqA723.jpeg', '                  ', 1, 'Ongoing', 'Completed', 1, 'Uttara', 'TEXTILE PALCE', 'Residential', 'Avaiable'),
(4, '2023-03-05', 202303053, '3', 'BANDON-3', '55,00,000', '1350', '', '', '3', '3', '3', '27.3 X 10.3', '      Beside sector 15,Uttara,Near Metro Rail 1ST STATION,Dhaka', '1', '9 x8', 'property_image/3.jpg', '', '            ', 1, 'Ongoing', 'Completed', 1, 'Uttara', 'BANDON-3', 'Residential', 'Avaiable'),
(5, '2023-03-05', 202303054, '2', 'SOUTH PALACE', '55,00,000', '1832', '', '', '333', '3', '3', '17.5 X 12.8', '       Beside sector 15,Uttara,Near Metro Rail 1ST station,Dhaka', '1', '10.00 X 7.5', 'property_image/WhatsApp Image 2023-02-27 at 12.59.38 PM.jpeg', 'property_banner/WhatsApp Image 2023-03-01 at 11.00.04 AM (2).jpeg', '              ', 1, 'Ongoing', 'Completed', 1, 'Uttara', 'SOUTH PALACE', 'Residential', 'Avaiable'),
(6, '2023-03-05', 202303055, '2', 'STI ORCHID', '47,00,000', '1532', '', '', '3', '3', '3', '13.5 X 13.5', '   Beside sector 15,Uttara,Near Metro Rail 1ST station,Dhaka', '1', '7.5 X 7.4', 'property_image/WhatsApp Image 2023-03-05 at 3.16.13 PM.jpeg', 'property_banner/WhatsApp Image 2023-03-01 at 11.00.04 AM (1).jpeg', '      ', 1, 'Upcoming', 'under construction', 1, 'Uttara', 'STI ORCHID', 'Residential', 'Avaiable'),
(7, '2023-03-05', 202303056, '2', 'STI ROSE GARDEN', '52,00,000', '1641', '', '', '3', '3', '3', '14.7 X 15.3', '  Beside sector 15,Uttara,Near Metro Rail 1ST station,Dhaka', '6', '10.00 X 9.2', 'property_image/2021-10-21.jpg', '', '    ', 1, 'Ongoing', 'Completed', 1, 'Uttara', 'STI ROSE GARDEN', 'Residential', 'Avaiable'),
(8, '2023-03-13', 202303131, '2', 'BANDON-6', '55,00,000', '1550', '', '', '3', '3', '3', '', '      Beside sector 15,Uttara,Near Metro Rail 1ST STATION,Dhaka', '1', '', 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM.jpeg', '', '      ', 1, 'Ongoing', 'Completed', 1, 'Uttara', 'BANDON-6', 'Residential', 'Avaiable'),
(9, '2023-03-13', 202303132, '2', 'BANDON-4', '55,00,000', '1850', '', '', '3', '3', '3', '', '      Beside sector 15,Uttara,Near Metro Rail 1ST STATION,Dhaka', '', '', 'property_image/Basic-Sunnydel-03-1-500x600.jpg', '', '      ', 1, 'Ongoing', 'Completed', 1, 'Uttara', 'BANDON-4', 'Residential', 'Avaiable'),
(10, '2023-03-13', 202303133, '1', 'S.I.PALACE', '58,00,000', '1524', '', '', '3', '3', '3', '16.0 X 9.0', '        Beside sector 15,Uttara,Near Metro Rail 1ST STATION,Dhaka', '1', '7.1 X 5.0', 'property_image/WhatsApp Image 2023-03-13 at 11.55.53 AM.jpeg', '', '          ', 1, 'Ongoing', 'under construction', 3, 'Uttara', 'S.I. PALACE', 'Residential', 'Avaiable'),
(11, '2023-03-13', 202303134, '2', 'COMPLEX -1', '55,00,000', '1700', '', '', '3', '3', '3', '16.10 x 11.1', '   Beside Sector-15,Neer Metro Rail 1ST STATION,Uttara ', '1', '7.8 x 8.1', 'property_image/1603692472.jpg', '', '        ', 1, 'Ongoing', 'under construction', 1, 'Uttara', 'COMPLEX -1', 'Residential', 'Avaiable'),
(12, '2023-03-13', 202303135, '2', 'COMPLEX -2', '55,00,000', '1570', '', '', '3', '3', '3', '18.1 x 11', '  Beside Sector-15,Neer Metro Rail 1ST STATION,Uttara ', '', '9.8 x 7.9', 'property_image/ec132a12af20895ab228e5e484c4f6e8.jpg', '', '    ', 1, 'Ongoing', 'under construction', 1, 'Uttara', 'COMPLEX -2', 'Residential', 'Avaiable'),
(13, '2023-03-13', 202303136, '2', 'COMPLEX -3', '50,00,000', '1560', '', '', '3', '3', '3', '18.1 x 11', '  Beside Sector-15,Neer Metro Rail 1ST STATION,Uttara ', '', '9.8 x 7.9', 'property_image/apartment-building-14-01.jpg', '', '    ', 1, 'Ongoing', 'under construction', 1, 'Uttara', 'COMPLEX -3', 'Residential', 'Avaiable'),
(14, '2023-03-13', 202303137, '2', 'BANDON-1', '46,00,000', '1750', '', '', '3', '3', '3', '16.0 X 9.0', '  Beside Sector-15,Neer Metro Rail 1ST STATION,Uttara ', '', '9.8 x 7.9', 'property_image/images (3).jpeg', '', '    ', 1, 'Ongoing', 'under construction', 1, 'Uttara', 'BANDON -1', 'Residential', 'Avaiable'),
(15, '2023-03-13', 202303138, '2', 'BANDON-2', '46,00,000', '1750', '', '', '3', '3', '3', '', '  Beside Sector-15,Neer Metro Rail 1ST STATION,Uttara ', '1', '9.8 x 7.9', 'property_image/popular3.jpg', '', '    ', 1, 'Ongoing', 'under construction', 1, 'Uttara', 'BANDON -2', 'Residential', 'Avaiable'),
(16, '2023-03-13', 202303139, '2', 'BANDON-5', '46,00,000', '1750', '', '', '3', '3', '3', '16.0 X 9.0', '   Beside Sector-15,Neer Metro Rail 1ST STATION,Uttara ', '1', '9.8 x 7.9', 'property_image/images (2).jpeg', '', '      ', 1, 'Ongoing', 'under construction', 1, 'Uttara', 'BANDON -5', 'Residential', 'Avaiable'),
(17, '2023-03-13', 202303140, '2', 'APON NIBAS', '46,00,000', '1965', '', '', '3', '3', '3', '16.10 x 11.1', ' Beside Sector-15,Neer Metro Rail 1ST STATION,Uttara ', '', '9.8 x 7.9', 'property_image/images (4).jpeg', '', '  ', 1, 'Ongoing', 'under construction', 1, 'Uttara', 'APON NIBAS', 'Residential', 'Avaiable'),
(18, '2023-03-13', 202303141, '3', 'STAR VIEW', '46,00,000', '1650', '', '', '3', '3', '3', '16.0 X 9.0', '    Beside Sector-15,Neer Metro Rail 1ST STATION,Uttara ', '', '9.8 x 7.9', 'property_image/popular3_nNKDRh7.jpg', 'property_banner/Honeymoon-Suite_resized.webp', '        ', 1, 'Completed', 'Completed', 1, 'Uttara', 'STAR VIEW', 'Residential', 'Avaiable');

-- --------------------------------------------------------

--
-- Table structure for table `property_propertyfacility`
--

CREATE TABLE `property_propertyfacility` (
  `id` bigint NOT NULL,
  `property_id` int DEFAULT NULL,
  `facility_icon` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `facility_name_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_propertyfacility`
--

INSERT INTO `property_propertyfacility` (`id`, `property_id`, `facility_icon`, `status`, `facility_name_id`) VALUES
(1, 202303051, '', 1, 1),
(2, 202303051, '', 1, 2),
(3, 202303051, '', 1, 4),
(4, 202303051, '', 1, 3),
(5, 202302261, '', 1, 1),
(6, 202302261, '', 1, 2),
(7, 202302261, '', 1, 3),
(8, 202302261, '', 1, 4),
(9, 202303052, '', 1, 1),
(10, 202303052, '', 1, 3),
(11, 202303052, '', 1, 4),
(12, 202303053, '', 1, 1),
(13, 202303053, '', 1, 2),
(14, 202303053, '', 1, 3),
(15, 202303053, '', 1, 4),
(16, 202303054, '', 1, 1),
(17, 202303054, '', 1, 2),
(18, 202303054, '', 1, 3),
(19, 202303054, '', 1, 4),
(20, 202303055, '', 1, 1),
(21, 202303055, '', 1, 3),
(22, 202303055, '', 1, 4),
(23, 202303056, '', 1, 1),
(24, 202303056, '', 1, 2),
(25, 202303056, '', 1, 3),
(26, 202303056, '', 1, 4),
(27, 202303132, '', 1, 1),
(28, 202303132, '', 1, 4),
(29, 202303131, '', 1, 1),
(30, 202303131, '', 1, 4),
(31, 202303133, '', 1, 1),
(32, 202303133, '', 1, 3),
(33, 202303133, '', 1, 4),
(34, 202303134, '', 1, 1),
(35, 202303134, '', 1, 3),
(36, 202303134, '', 1, 4),
(37, 202303135, '', 1, 1),
(38, 202303135, '', 1, 2),
(39, 202303135, '', 1, 3),
(40, 202303135, '', 1, 4),
(41, 202303136, '', 1, 1),
(42, 202303136, '', 1, 2),
(43, 202303136, '', 1, 3),
(44, 202303136, '', 1, 4),
(45, 202303137, '', 1, 1),
(46, 202303137, '', 1, 2),
(47, 202303137, '', 1, 3),
(48, 202303138, '', 1, 1),
(49, 202303138, '', 1, 2),
(50, 202303138, '', 1, 3),
(51, 202303138, '', 1, 4),
(52, 202303139, '', 1, 1),
(53, 202303139, '', 1, 2),
(54, 202303140, '', 1, 1),
(55, 202303140, '', 1, 3),
(56, 202303140, '', 1, 4),
(57, 202303141, '', 1, 1),
(58, 202303141, '', 1, 2),
(59, 202303141, '', 1, 3),
(60, 202303141, '', 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `property_propertyownership`
--

CREATE TABLE `property_propertyownership` (
  `id` bigint NOT NULL,
  `property_id` int DEFAULT NULL,
  `property_owner_name` varchar(200) NOT NULL,
  `property_ownership` varchar(300) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_propertyownership`
--

INSERT INTO `property_propertyownership` (`id`, `property_id`, `property_owner_name`, `property_ownership`, `status`) VALUES
(106, 202303051, 'STI  BUILDERS LTD', '', 1),
(107, 202303052, '', '', 1),
(108, 202303053, '', '', 1),
(109, 202303054, '', '', 1),
(110, 202303055, '', '', 1),
(111, 202303056, '', '', 1),
(112, 202303131, '', '', 1),
(115, 202302261, '', '50 %', 1),
(116, 202302261, '', '25 %', 1),
(117, 202303132, '', '', 1),
(119, 202303134, '', '', 1),
(120, 202303135, '', '', 1),
(121, 202303136, '', '', 1),
(122, 202303137, '', '', 1),
(123, 202303138, '', '', 1),
(124, 202303139, '', '', 1),
(125, 202303140, '', '', 1),
(127, 202303141, '', '', 1),
(128, 202303133, '', '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_propertyphoto`
--

CREATE TABLE `property_propertyphoto` (
  `id` bigint NOT NULL,
  `property_id` int DEFAULT NULL,
  `property_photo` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_propertyphoto`
--

INSERT INTO `property_propertyphoto` (`id`, `property_id`, `property_photo`, `status`) VALUES
(1, 202302261, 'property_photo/WhatsApp Image 2023-02-26 at 5.42.05 PM (1).jpeg', 1),
(2, 202302261, 'property_image/interior.jpg', 1),
(3, 202302261, 'property_image/interior-1_l7j2wes.jpg', 1),
(4, 202302261, 'property_image/interior-2.jpg', 1),
(5, 202303051, 'property_image/WhatsApp Image 2023-02-27 at 12.59.53 PM_dN83fyp.jpeg', 1),
(6, 202303051, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.05 AM (5).jpeg', 1),
(7, 202303051, 'property_photo/3fc45109-43ff-4834-9f44-0dd647339b74.jfif', 1),
(8, 202303051, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.04 AM (7).jpeg', 1),
(9, 202303052, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.26 AM (1).jpeg', 1),
(10, 202303052, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.05 AM (11).jpeg', 1),
(11, 202303052, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.05 AM (7).jpeg', 1),
(12, 202303052, 'property_photo/WhatsApp Image 2023-02-26 at 4.28.59 PM (1).jpeg', 1),
(13, 202303053, 'property_photo/3.jpg', 1),
(14, 202303053, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.04 AM (5).jpeg', 1),
(15, 202303053, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.04 AM (4).jpeg', 1),
(16, 202303053, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.04 AM (5)_8PoYB0S.jpeg', 1),
(17, 202303053, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.05 AM (3).jpeg', 1),
(18, 202303053, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.05 AM (11)_JHlPSgH.jpeg', 1),
(19, 202303054, 'property_photo/WhatsApp Image 2023-02-27 at 12.59.38 PM.jpeg', 1),
(20, 202303054, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.05 AM (1).jpeg', 1),
(21, 202303054, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.04 AM (5)_ZyisSCs.jpeg', 1),
(22, 202303054, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.05 AM (4).jpeg', 1),
(23, 202303055, 'property_photo/WhatsApp Image 2023-03-05 at 3.16.13 PM.jpeg', 1),
(24, 202303055, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.04 AM (4)_iNDvlt4.jpeg', 1),
(25, 202303055, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.05 AM (5)_oEFEXOx.jpeg', 1),
(26, 202303055, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.04 AM (8).jpeg', 1),
(27, 202303055, 'property_photo/WhatsApp Image 2023-03-01 at 11.00.05 AM (1)_i35xwCu.jpeg', 1),
(28, 202303056, 'property_image/3fc45109-43ff-4834-9f44-0dd647339b74.jfif', 1),
(29, 202303056, 'property_image/WhatsApp Image 2023-03-01 at 11.00.04 AM (6).jpeg', 1),
(30, 202303056, 'property_image/WhatsApp Image 2023-03-01 at 11.00.05 AM (2).jpeg', 1),
(31, 202303056, 'property_image/2021-10-21_pUE3NY6.jpg', 1),
(32, 202303133, 'property_photo/WhatsApp Image 2023-03-13 at 11.28.27 AM (5).jpeg', 1),
(33, 202303133, 'property_photo/WhatsApp Image 2023-03-13 at 11.28.27 AM (9).jpeg', 1),
(34, 202303133, 'property_photo/WhatsApp Image 2023-03-13 at 11.28.27 AM (11).jpeg', 1),
(35, 202303134, 'property_photo/WhatsApp Image 2023-03-13 at 11.28.27 AM (3).jpeg', 1),
(36, 202303134, 'property_photo/WhatsApp Image 2023-03-13 at 11.28.27 AM (11)_RvJ9XF8.jpeg', 1),
(37, 202303134, 'property_photo/WhatsApp Image 2023-03-13 at 11.28.27 AM (17).jpeg', 1),
(38, 202303135, 'property_image/874965782_71ecdcd81e_b.jpg', 1),
(39, 202303135, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (4).jpeg', 1),
(40, 202303135, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (1).jpeg', 1),
(41, 202303136, 'property_image/ab26a8ec9c76ee9f99bba3cd3994e99d.jpg', 1),
(42, 202303136, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (8).jpeg', 1),
(43, 202303136, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (1)_GkXRqVr.jpeg', 1),
(44, 202303137, 'property_image/Bedroom_Mitcham.jpg', 1),
(45, 202303137, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (2).jpeg', 1),
(46, 202303137, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (17).jpeg', 1),
(47, 202303138, 'property_image/bedroom-colour-combination-with-burnt-orange-and-purple-1-768x512.jpg', 1),
(48, 202303138, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (9).jpeg', 1),
(49, 202303138, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (1)_XCoe9Rx.jpeg', 1),
(50, 202303139, 'property_image/bedroom-colour-combination-with-burnt-orange-and-purple-1-768x512_e36mCJa.jpg', 1),
(51, 202303139, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (14).jpeg', 1),
(52, 202303139, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (1)_YIDQ9Se.jpeg', 1),
(53, 202303140, 'property_image/ceara-donnelley-charleston-house-tour-bedroom-jpg-1618427139.jpg', 1),
(54, 202303140, 'property_image/Vincent_Dining_Table_Walnut_Joshua_Chair_5.webp', 1),
(55, 202303140, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (16).jpeg', 1),
(56, 202303141, 'property_image/Honeymoon-Suite.jpg', 1),
(57, 202303141, 'property_image/WhatsApp Image 2023-03-13 at 11.28.27 AM (8)_cVSOII9.jpeg', 1),
(58, 202303141, 'property_image/images (5).jpeg', 1),
(59, 202302261, 'property_photo/honeymoon-bed-decoration.jpg', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_propertytype`
--

CREATE TABLE `property_propertytype` (
  `id` bigint NOT NULL,
  `property_type` varchar(300) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_propertytype`
--

INSERT INTO `property_propertytype` (`id`, `property_type`, `logo`, `status`) VALUES
(1, 'Residential', 'images/property_type_logo/icons8-residential-1001_oXTOWib.png', 1),
(2, 'Commercial', 'images/property_type_logo/Commercial_a4v6hM8.png', 1),
(3, 'Integrated', 'images/property_type_logo/Integrated_kDCvElK.png', 1),
(4, 'Land Sharing', 'images/property_type_logo/Land-Sharing_yAIGgIG.png', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_propertyvideo`
--

CREATE TABLE `property_propertyvideo` (
  `id` bigint NOT NULL,
  `property_id` int DEFAULT NULL,
  `property_video_rul` longtext NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_propertyvideo`
--

INSERT INTO `property_propertyvideo` (`id`, `property_id`, `property_video_rul`, `status`) VALUES
(87, 202303051, '', 1),
(88, 202303052, '', 1),
(89, 202303053, '', 1),
(90, 202303054, '', 1),
(91, 202303055, '', 1),
(92, 202303056, '', 1),
(93, 202303131, '', 1),
(95, 202302261, '', 1),
(96, 202303132, '', 1),
(98, 202303134, '', 1),
(99, 202303135, '', 1),
(100, 202303136, '', 1),
(101, 202303137, '', 1),
(102, 202303138, '', 1),
(103, 202303139, '', 1),
(104, 202303140, '', 1),
(106, 202303141, '', 1),
(107, 202303133, '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `property_salesstatus`
--

CREATE TABLE `property_salesstatus` (
  `id` bigint NOT NULL,
  `sales_status` varchar(300) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `property_salesstatus`
--

INSERT INTO `property_salesstatus` (`id`, `sales_status`, `status`) VALUES
(1, 'Avaiable', 1),
(2, 'Booked', 1),
(3, 'Sold', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_affiliatesupplieradd`
--

CREATE TABLE `realstateapp_affiliatesupplieradd` (
  `id` bigint NOT NULL,
  `name` varchar(500) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_certifiedadd`
--

CREATE TABLE `realstateapp_certifiedadd` (
  `id` bigint NOT NULL,
  `certified_title` varchar(500) NOT NULL,
  `certified_text` longtext NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_certifiedadd`
--

INSERT INTO `realstateapp_certifiedadd` (`id`, `certified_title`, `certified_text`, `status`) VALUES
(1, 'Certified Real Estate Company in Bangladesh', 'As recognition of creating and maintaining a working standard and valuing & distinguishing each department. This recognition further inspires us to maintain quality and creating a higher standard in the real estate industry in Bangladesh. As a REHAB member, we are committed to being conscious about the selection of project sites, using quality construction materials, modern fittings, and maintaining uncompromising standards..', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_chairmessage`
--

CREATE TABLE `realstateapp_chairmessage` (
  `id` bigint NOT NULL,
  `name` varchar(500) NOT NULL,
  `designation` varchar(500) NOT NULL,
  `image` varchar(100) NOT NULL,
  `message` longtext NOT NULL,
  `facebook_link` varchar(200) NOT NULL,
  `twitter_link` varchar(200) NOT NULL,
  `instragram_link` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_chairmessage`
--

INSERT INTO `realstateapp_chairmessage` (`id`, `name`, `designation`, `image`, `message`, `facebook_link`, `twitter_link`, `instragram_link`, `status`) VALUES
(1, 'Md. Eshaq Ali', 'MANAGING DIRECTOR', 'message_image/WhatsApp Image 2023-04-09 at 1.28.38 PM (1).jpeg', '     I would like to begin by expressing the satisfaction of being capable of conveying the values that the Arisha institution, promised to hold on the primary day it began to work till nowadays with its revel in of greater than 10 years. We began out all our commercial enterprise understanding that we need to add value to our country. We have witnessed, by experiencing, that each work carried out with love, constantly looking after the good, can bring about success without dropping faith. Today, STI Builders is a big company serving in specific sectors which include construction, buildings, land share, engineering, and agro fisheries, and you, who take care of us and feel responsible, have a superb share in this. Our precious business partners, customers, and really valuable colleagues; will hold to work and produce to gain the future of our country. We will constantly keep our dreams at the best level to contribute to the economy and employment of our country, that&#39;s taking corporate steps toward becoming the world&rsquo;s great power. Maintaining our determination on the road to our dreams ought to only be feasible with the value you added. Thank you very much for your belief in us.     ', '', '', '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_companyprofile`
--

CREATE TABLE `realstateapp_companyprofile` (
  `id` bigint NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `slugan` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(15) DEFAULT NULL,
  `mobile1` varchar(15) DEFAULT NULL,
  `phone1` varchar(15) DEFAULT NULL,
  `address` longtext,
  `about` longtext,
  `staring_year` int NOT NULL,
  `google_map_link` longtext,
  `copy_right` varchar(50) DEFAULT NULL,
  `facebook_link` varchar(200) DEFAULT NULL,
  `twitter_link` varchar(200) DEFAULT NULL,
  `linkedin_link` varchar(200) DEFAULT NULL,
  `youtube_link` varchar(200) DEFAULT NULL,
  `whatsapp_link` varchar(200) DEFAULT NULL,
  `instragram_link` varchar(200) DEFAULT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_companyprofile`
--

INSERT INTO `realstateapp_companyprofile` (`id`, `company_name`, `logo`, `slugan`, `email`, `mobile`, `mobile1`, `phone1`, `address`, `about`, `staring_year`, `google_map_link`, `copy_right`, `facebook_link`, `twitter_link`, `linkedin_link`, `youtube_link`, `whatsapp_link`, `instragram_link`, `status`) VALUES
(1, 'STI Builders Limited', 'logo/sti-logo_zX6ysKb.png', 'None', 'stibuilders@gmail.com', '01923505050', '01322301173', NULL, 'House#41 (Flat-A5,L-05), Sector#12, Uttara Model Town, Dhaka-1230', '<p><strong>STI Builders LTD</strong>, a multi-disciplinary business house, has established itself to be a dynamic and revolutionary enterprise, positioning itself as one of the central business houses withinside the country. We are working to attain being the best brand devoted to excellence in all our endeavors &amp;ndash; our long-term control vision. This requires us to create a strong platform to hand over constant increases under any condition.</p>\r\n\r\n<p><strong>STI Builders LTD </strong>is one of the top civil construction companies in the country. We achieved this leading position through our continued hard labor, excellent teamwork, and perfect project-making experience. Our efforts gave us a unique organization. Our marketing team has a vast knowledge of supporting and satisfying our clients. Their significant expertise helps to handle large projects smoothly. We always keep the priority on our customers &amp; demand.</p>\r\n\r\n<p>By the Grace of the Almighty, we are certainly privileged to have acquired the most powerful of platforms as presented by our founding directors. They have provided us with a wholesome financial base, robust asset backing, a corporation without debt and liabilities, timely and forward-thinking succession planning, and lastly, undeniable popularity withinside the market.</p>\r\n', 2011, 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3648.4409906304654!2d90.3777743137588!3d23.87397628452862!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3755c51ded153155%3A0xdf48ef432c1b78ae!2sSTI%20Builders%20Ltd!5e0!3m2!1sen!2sbd!4v1669002892459!5m2!1sen!2sbd', NULL, 'https://www.facebook.com/stibuilders', 'None', 'None', 'None', NULL, 'None', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_contactmessage`
--

CREATE TABLE `realstateapp_contactmessage` (
  `id` bigint NOT NULL,
  `name` varchar(500) NOT NULL,
  `email` varchar(254) NOT NULL,
  `property_plot_type` varchar(1500) NOT NULL,
  `location` varchar(1500) NOT NULL,
  `apartment_size` varchar(1500) NOT NULL,
  `message` longtext NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_contactmessage`
--

INSERT INTO `realstateapp_contactmessage` (`id`, `name`, `email`, `property_plot_type`, `location`, `apartment_size`, `message`, `status`) VALUES
(1, 'GeorgeWoota', 'al.berthanshin.49@gmail.com', 'al.berthanshin.49@gmail.com', 'Kuwait', 'Kuwait', 'Mjfejdjwdjiwdhwsuf hohaufheodajidhowaf hwidjidjqiohfuehooiPQKWODJQIJ IWJDOKDOWJDIjefiwjreir jwqifjweifewifeefjrghr jfejfekwlfjrghwjwajkdjwfew stibuilderslimited.com', 1),
(2, 'Kali Bustos', 'kali.bustos@gmail.com', 'kali.bustos@gmail.com', '', '', 'I can blast your ad text to millions of website contact forms. One flat rate, never any per click costs. People will read your message just like you\'re reading this one that I just sent through your website contact form now. Shoot me a quick email here for the details : nixhexx007@boranora.com', 1),
(3, 'RaymondHouby', 'no.reply.GerhardTaylor@gmail.com', 'no.reply.GerhardTaylor@gmail.com', 'United Arab Emirates', 'United Arab Emirates', 'Yo! stibuilderslimited.com \r\n \r\nDid you know that it is possible to send message effectively and legally? We are making available a unique method of sending business offers through feedback forms. There are a great many websites with these forms available. \r\nWhen such proposals are submitted, no personal information is utilized, and messages are routed to forms specifically configured to receive messages and appeals securely. Feedback Forms\' messages are thought of as significant thus avoiding the categorization of them as spam. \r\nCome and sample our service without any cost! \r\nYou can rely on us to send up to 50,000 messages. \r\n \r\nThe cost of sending one million messages is $59. \r\n \r\nThis message was automatically generated. \r\nPlease use the contact details below to get in touch with us. \r\n \r\nContact us. \r\nTelegram - https://t.me/FeedbackFormEU \r\nSkype  live:feedbackform2019 \r\nWhatsApp  +375259112693 \r\nWhatsApp  https://wa.me/+375259112693 \r\n \r\nWe only use chat for communication.', 1),
(4, 'RobertgEm', 'a.l.b.e.rth.a.n.s.h.in49@gmail.com', 'a.l.b.e.rth.a.n.s.h.in49@gmail.com', 'Kenya', 'Kenya', '<html><a href=\"https://google.com\"><img src=\"https://blogger.googleusercontent.com/img/a/AVvXsEgXM4xrSRAnQQOLZImSaLdACcB-BosbLfsYEsXB-lLBl71Ma4AFA4xbB22ruqkub9W8nQCJVUXuXvJQeNLG2yoUL-OxTbhSvuyduxRSQI5RsQSu6DbfkMCVMuCuRB1uzs4KNkp3gZjcKQeubD_3RZ6p3xDAEpOwy6LnNnGhSa3h4V04dq3zc3oZajp_=s16000\"></a></br> stibuilderslimited.com ugerufeijdjefejdjiefjeofkoefjegjefdwifjefgeijdfiewgjiejdwsfhefrgerreytr</html>', 1),
(5, 'Mozelle Mondragon', 'hacker@4x4snorkels.com', 'hacker@4x4snorkels.com', '', '', 'We have hacked your website stibuilderslimited.com and extracted your databases. This was due to the security holes you had in your your site/server which have gained us remote control of everything that was on the server. \r\n\r\nOur team is mostly interested in customer, administrative, and employee information which we have extracted through your databases once we got remote control over the server. It still needs to be sorted out but it will be well-organized once finished. First, we will be going through the emails/sms information and contacting the recipient how you held in disregard about their information being exposed to a hacking group when you could have stopped it. This would be detrimental to your personal image with these relationships with these people. Lastly, now that we have information not only will we be monetizing off it with our methods but made public or sold to other people that will do whatever they wish with the information also after we are done.\r\n\r\nNow you can put a stop to this by paying a $3000 fee (0.10 BTC) in bitcoin to the address 37J6b5DADjC5WubZX5PCGNTg2WXjdVa3Fa We will be notified of payment which we will then delete the information we have obtained, patch the hole in the site/server which we got in and remove you from any future targeting in the future. You have 72 hours in doing so after viewing this message or the series of steps will commence. You can obtain bitcoin through such services such as paxful.com or do a search on bing.com', 1),
(6, 'Hello World! https://racetrack.top/go/giywczjtmm5dinbs?hs=c6bfed29f62cff2d471ead27a6a8dc8f&', 'ayfkuh@tofeat.com', 'zzcjc5', '2v2zi9', '63ul5l', '8vrh2j', 1),
(7, 'DouglasBic', '', '', 'Denmark', 'Denmark', 'Elite SMM Services - Your Secret Weapon for Social Media Success https://smm-elite-service.leybakapalabo.tk/invite-3969', 1),
(8, 'Daksh Adhyaru', 'darshak@itztotalsolutions.com', 'darshak@itztotalsolutions.com', '', '', 'Hey there,\r\n\r\nI’m writing in hopes of finding the appropriate person who handles business development or sales department. So if it makes sense to talk, let me know how your calendar looks.\r\n\r\nI noticed that your company provides real estate related services. We help companies with title searching, title plant indexing, and data management services. So, if you have any requirements related to it. Do let us know.\r\n\r\nIf you want to look at our title searching, data entry or title plant indexing samples? Don\'t hesitate to reach me.\r\n\r\nSome of our clients include ProTitle USA, iiExperts, LLC, and Reid & Associates.\r\n\r\nIf you are the appropriate person to speak with, what does your calendar look like?\r\n\r\nIf not, who do you recommend I talk to?\r\n\r\nThanks,\r\nDarshak Adhyaru\r\nPresident of Operations\r\nITZ Total Solutions\r\nEmail: darshak@itztotalsolutions.com', 1),
(9, 'Mike Wesley\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'United States', 'United States', 'Hi there \r\n \r\nJust checked your stibuilderslimited.com in MOZ and saw that you could use an authority boost. \r\n \r\nWith our service you will get a guaranteed Domain Authority score within just 3 months time. This will increase the organic visibility and strengthen your website authority, thus getting it stronger against G updates as well. \r\n \r\nFor more information, please check our offers \r\nhttps://www.monkeydigital.co/domain-authority-plan/ \r\n \r\nNEW: Semrush DA is now possible \r\nhttps://www.monkeydigital.co/semrush-da/ \r\n \r\nThanks and regards \r\nMike Wesley\r\n', 1),
(10, 'Mike Vaughan\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'Taiwan', 'Taiwan', 'Hi \r\n \r\nI have just took a look on your SEO for  stibuilderslimited.com for the ranking keywords and saw that your website could use a push. \r\n \r\nWe will increase your ranks organically and safely, using state of the art AI and whitehat methods, while providing monthly reports and outstanding support. \r\n \r\nMore info: \r\nhttps://www.hilkom-digital.de/cheap-seo-packages/ \r\n \r\nRegards \r\nMike Vaughan\r\n', 1),
(11, 'Daksh Adhyaru', 'darshak@itztotalsolutions.com', 'darshak@itztotalsolutions.com', '', '', 'Hey there,\r\n\r\nI’m writing in hopes of finding the appropriate person who handles business development or sales department. So if it makes sense to talk, let me know how your calendar looks.\r\n\r\nI noticed that your company provides real estate related services. We help companies with title searching, title plant indexing, and data management services. So, if you have any requirements related to it. Do let us know.\r\n\r\nIf you want to look at our title searching, data entry or title plant indexing samples? Don\'t hesitate to reach me.\r\n\r\nSome of our clients include ProTitle USA, iiExperts, LLC, and Reid & Associates.\r\n\r\nIf you are the appropriate person to speak with, what does your calendar look like?\r\n\r\nIf not, who do you recommend I talk to?\r\n\r\nThanks,\r\nDarshak Adhyaru\r\nPresident of Operations\r\nITZ Total Solutions\r\nEmail: darshak@itztotalsolutions.com', 1),
(12, 'Mike Barnes\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'United States', 'United States', 'Hi \r\n \r\nI have just analyzed  stibuilderslimited.com for onsite errors and saw that your website has a handful of issues which should be addressed. \r\n \r\nNo matter what you are offering or selling, having a poor optimized site, full of bugs and errors, will never help your ranks. \r\n \r\nLet us fix your wordpress site errors today and get your ranks reach their full potential \r\n \r\nMore info: \r\nhttps://www.digital-x-press.com/product/wordpress-seo-audit-and-fix-service/ \r\n \r\n \r\nRegards \r\nMike Barnes\r\n', 1),
(13, 'Gary Wilson', 'gw2920339@gmail.com', 'gw2920339@gmail.com', 'United Kingdom', 'United Kingdom', 'Good day, \r\n \r\nI am reaching out to express my interest in a potential business opportunity that worth $26.8 Million. \r\nThis would be of a great benefit to both parties if handled well. \r\n \r\nPlease get back to me through this email: Gw455075@gmail.com \r\n \r\nThanks, \r\n \r\nGary Wilson', 1),
(14, 'Mike Thorndike\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'Netherlands Antilles', 'Netherlands Antilles', 'Greetings \r\n \r\nThis is Mike Thorndike\r\n \r\nLet me show you our latest research results from our constant SEO feedbacks that we have from our plans: \r\n \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nThe new Semrush Backlinks, which will make your stibuilderslimited.com SEO trend have an immediate push. \r\nThe method is actually very simple, we are building links from domains that have a high number of keywords ranking for them.  \r\n \r\nForget about the SEO metrics or any other factors that so many tools try to teach you that is good. The most valuable link is the one that comes from a website that has a healthy trend and lots of ranking keywords. \r\nWe thought about that, so we have built this plan for you \r\n \r\nCheck in detail here: \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nCheap and effective \r\n \r\nTry it anytime soon \r\n \r\n \r\nRegards \r\n \r\nMike Thorndike\r\n \r\nmike@strictlydigital.net', 1),
(15, 'Mike Palmer\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'New Zealand', 'New Zealand', 'If you have a local business and want to rank it on google maps in a specific area then this service is for you. \r\n \r\nGoogle Map Stacking is one of the best ways to rank your GMB in a specific mile radius. \r\n \r\nMore info: \r\nhttps://www.speed-seo.net/product/google-maps-pointers/ \r\n \r\nThanks and Regards \r\nMike Palmer\r\n \r\n \r\nPS: Want an all in one Local Plan that includes everything? \r\nhttps://www.speed-seo.net/product/local-seo-package/', 1),
(16, 'Josephseato', 'no.reply.DidierJansen@gmail.com', 'no.reply.DidierJansen@gmail.com', 'Nicaragua', 'Nicaragua', 'Greetings! stibuilderslimited.com \r\n \r\nDid you know that it is possible to send business offers completely legal? We propose a new method of submitting appeals via feedback forms. Feedback forms like these can be seen on a host of websites. \r\nWhen such business offers are sent, no personal data is used, and messages are sent to forms specifically designed to receive messages and appeals safely and securely. Contact Form messages are usually not sent to spam, since they are considered to be important. \r\nWe offer you to try our service for free. \r\nWe will provide up to 50,000 messages to you. \r\n \r\nThe cost of sending one million messages is $59. \r\n \r\nThis message was automatically generated. \r\nPlease use the contact details below to get in touch with us. \r\n \r\nContact us. \r\nTelegram - https://t.me/FeedbackFormEU \r\nSkype  live:feedbackform2019 \r\nWhatsApp  +375259112693 \r\nWhatsApp  https://wa.me/+375259112693 \r\n \r\nWe only use chat for communication.', 1),
(17, 'Maude Case', 'hacker@ognisty.eu', 'hacker@ognisty.eu', '', '', 'We have hacked your website stibuilderslimited.com and extracted your databases. This was due to the security holes you had in your your site/server which have gained us remote control of everything that was on the server. \r\n\r\nOur team is mostly interested in customer, administrative, and employee information which we have extracted through your databases once we got remote control over the server. It still needs to be sorted out but it will be well-organized once finished. First, we will be going through the emails/sms information and contacting the recipient how you held in disregard about their information being exposed to a hacking group when you could have stopped it. This would be detrimental to your personal image with these relationships with these people. Lastly, now that we have information not only will we be monetizing off it with our methods but made public or sold to other people that will do whatever they wish with the information also after we are done.\r\n\r\nNow you can put a stop to this by paying a $3000 fee (0.11 BTC) in bitcoin. You can find our address by visiting https://www.blockchain.com/explorer/addresses/btc/39PHuTwgY5THshy9VJoUXWebDA5jCprPmP where you can copy and paste the address or scan the QR code. We will be notified of payment which we will then delete the information we have obtained, patch the hole in the site/server which we got in and remove you from any future targeting in the future. You have 72 hours in doing so after viewing this message or the series of steps will commence. You can obtain bitcoin through such services such as paxful.com or do a search on bing.com', 1),
(18, 'Mike Winter\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'United States', 'United States', 'Hi there \r\n \r\nJust checked your stibuilderslimited.com in MOZ and saw that you could use an authority boost. \r\n \r\nWith our service you will get a guaranteed Domain Authority score within just 3 months time. This will increase the organic visibility and strengthen your website authority, thus getting it stronger against G updates as well. \r\n \r\nFor more information, please check our offers \r\nhttps://www.monkeydigital.co/domain-authority-plan/ \r\n \r\nNEW: Semrush DA is now possible \r\nhttps://www.monkeydigital.co/semrush-da/ \r\n \r\nThanks and regards \r\nMike Winter\r\n', 1),
(19, 'Mike Milton\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'Taiwan', 'Taiwan', 'Howdy \r\n \r\nI have just verified your SEO on  stibuilderslimited.com for its SEO Trend and saw that your website could use an upgrade. \r\n \r\nWe will increase your ranks organically and safely, using state of the art AI and whitehat methods, while providing monthly reports and outstanding support. \r\n \r\nMore info: \r\nhttps://www.hilkom-digital.de/cheap-seo-packages/ \r\n \r\nRegards \r\nMike Milton\r\n', 1),
(20, 'Mike Hamphrey\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'United States', 'United States', 'Hi there \r\n \r\nI have just verified your  stibuilderslimited.com for the current onsite SEO status and saw that your website has a handful of issues which should be addressed. \r\n \r\nNo matter what you are offering or selling, having a poor optimized site, full of bugs and errors, will never help your ranks. \r\n \r\nLet us fix your wordpress site errors today and get your ranks reach their full potential \r\n \r\nMore info: \r\nhttps://www.digital-x-press.com/product/wordpress-seo-audit-and-fix-service/ \r\n \r\n \r\nRegards \r\nMike Hamphrey\r\n', 1),
(21, 'GrantImasp', 'yasen.krasen.13+92309@mail.ru', 'yasen.krasen.13+92309@mail.ru', 'Marshall Islands', 'Marshall Islands', 'Ufieuhdidhefh wjdwdjqwidjwefhwfakj oijofqwfbvsdfjfwej ijwqiofjewuhfwedjawdhewh ouhwidwjpouweiofeiouqwruio ioqwiwuifewifjfifhw jiwfjiewhfewgiewufewio stibuilderslimited.com', 1),
(22, 'Mike Douglas\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'Netherlands Antilles', 'Netherlands Antilles', 'Howdy \r\n \r\nThis is Mike Douglas\r\n \r\nLet me introduce to you our latest research results from our constant SEO feedbacks that we have from our plans: \r\n \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nThe new Semrush Backlinks, which will make your stibuilderslimited.com SEO trend have an immediate push. \r\nThe method is actually very simple, we are building links from domains that have a high number of keywords ranking for them.  \r\n \r\nForget about the SEO metrics or any other factors that so many tools try to teach you that is good. The most valuable link is the one that comes from a website that has a healthy trend and lots of ranking keywords. \r\nWe thought about that, so we have built this plan for you \r\n \r\nCheck in detail here: \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nCheap and effective \r\n \r\nTry it anytime soon \r\n \r\n \r\nRegards \r\n \r\nMike Douglas\r\n \r\nmike@strictlydigital.net', 1),
(23, 'Martin Barreiro', 'wmueller831@gmail.com', 'wmueller831@gmail.com', 'Iceland', 'Iceland', 'Gunten Tag, \r\n \r\nMein Name ist Martin Barreiro, Ich habe Ihnen zuvor eine Nachricht bezuglich einer Transaktion in Hohe von 13, 5 Millionen US-Dollar gesendet, die mein verstorbener Kunde vor seinem plotzlichen Tod hinterlassen hat. \r\n \r\nIch melde mich noch einmal bei Ihnen, da ich nach Durchsicht Ihres Profils fest davon uberzeugt bin, dass Sie die Transaktion sehr gut mit mir abwickeln konnen. \r\nWenn Sie interessiert sind, mochte ich darauf hinweisen, dass nach der Transaktion 10% dieses Geldes unter Wohltatigkeitsorganisationen aufgeteilt werden sollen, wahrend die restlichen 90% zwischen uns aufgeteilt werden, also jeweils 45%. \r\n \r\nDiese Transaktion ist zu 100% risikofrei. Bitte antworten Sie mir so schnell wie moglich, um weitere Erlauterungen zur Transaktion zu erhalten, meine E-mail: martinjoselaw@proton.me \r\n \r\nHochachtungsvoll, Ich hoffe von Ihnen so schnell wie moglich zu horen \r\n \r\nMit freundlichen Grussen. \r\nMartin Barreiro, \r\nRechtsanwalt. \r\nTel. +34 661 220 756 \r\nE-mail: martinjose@bareiroabogados.com', 1),
(24, 'Wesley Tatum', 'wesley.tatum@gmail.com', 'wesley.tatum@gmail.com', '', '', 'Hi,\r\n\r\nAre you ready to embark on an exciting journey into the world of cryptocurrency? We are thrilled to invite you to register for a free crypto wallet, where you can securely store and manage your digital assets.\r\n\r\nHere at Binance, we believe that cryptocurrency has the potential to revolutionize the way we transact, invest, and build wealth. Whether you\'re a seasoned crypto enthusiast or just curious about this emerging technology, our free crypto wallet is the perfect starting point to explore the possibilities and take control of your financial future.\r\n\r\nWhy should you register for our free crypto wallet?\r\n\r\n► Secure and User-Friendly: Our wallet incorporates state-of-the-art security features to safeguard your digital assets. With a user-friendly interface, it\'s easy to navigate, even if you\'re new to the world of cryptocurrencies.\r\n\r\n► Convenience: Enjoy instant access to your funds anytime, anywhere. Say goodbye to the limitations of traditional banking hours and complicated procedures. Our wallet is designed to simplify your crypto experience.\r\n\r\n► Versatile Asset Support: Store and manage a wide range of cryptocurrencies in one place. Bitcoin, Ethereum, Ripple, Litecoin, and many more are supported, ensuring you have the flexibility to diversify your portfolio.\r\n\r\n► Peace of Mind: We prioritize the safety and security of your funds. Our wallet utilizes advanced encryption techniques, two-factor authentication, and cold storage to provide you with peace of mind and protect your assets from unauthorized access.\r\n\r\n► Exclusive Benefits: As a registered user, you\'ll gain access to exclusive benefits, including early access to new features, educational resources, and exclusive promotions. Stay ahead of the curve and maximize your crypto potential.\r\n\r\nDon\'t miss out on this incredible opportunity to step into the world of cryptocurrencies. Register for your free crypto wallet today and take control of your financial destiny!\r\n\r\nClick the link below to create your free crypto wallet:\r\nGet Started here >>> https://bit.ly/cryptowalletreg\r\n\r\n* Limited Time $100 FREE BONUS for any new account that Completes Account Verification. (Expires on 15th June 2023)\r\n\r\nJoin the millions of individuals who are already harnessing the power of cryptocurrencies. Secure your financial future with our free crypto wallet today!\r\n\r\nTo your financial success\r\n\r\nRonald D\r\n99 Manhatten Road, TX\r\n87845\r\n=====\r\nClick here to unsubscribe\r\nhttps://bit.ly/stop69', 1),
(25, 'Emilia Retzlaff', 'emilia.retzlaff@gmail.com', 'emilia.retzlaff@gmail.com', '', '', 'Hi,\r\n\r\nHow would you like to have a Most Advanced Ai assistant that can help you create 4K HD high-quality Video, graphics, and respond like a human?\r\n\r\nWell, your wish has come true! \r\n\r\nIntroducing…\r\n\r\nAi Diffusion - The world’s Ai App Create ..\r\nUltra HD Ai Videos, 4K HD Ai Images, Ai Cartoon Videos, \"Ai Diffusion Videos, Ai Animated Videos, Ai Drawings & Art, Ai Sketch Images, Images To 3D Videos, Ai Logos & Graphics And So Much More... \r\n\r\n������ Generate Ultra-HD 4k Videos & Images...\r\n������ Convert Any Video Into Ai Cartoons & Anime Videos In 1-Click...\r\n������ Generate Unlimited Ai Videos In Any Niche Just With A Single Keyword...\r\n������ Comes With Built-in Ai Video & Image Background Remover...\r\n������ Turn Any Normal Image Into Sketch With Just A Single Click...\r\n������ Convert Any Image Into 3D Video In Blink Of An Eye...\r\n������ Built-in GTA V Art & Video Style Maker...\r\n������ Image Inpainting\r\n������ Image Super Resolution\r\n������ Image Colorization\r\n������ Black & White To Color Video\r\n������ Video Background Color Changer\r\n������ Ai Cartoon Generator\r\n������ Night Image Enhancement\r\n..and much more\r\n\r\n\r\nWith Ai Diffusion, you can now spend less time stressing about your creative work and more time doing what you love!\r\n\r\nAnd the best part? \r\n\r\nAi Diffusion is easy to use! \r\n\r\n>> Go & check it out before they take it down...\r\nhttps://bit.ly/aidiffusion23\r\n\r\nRegards\r\n\r\nRonald D\r\n99 Manhatten Road, TX\r\n87845\r\n=====\r\nClick here to unsubscribe\r\nhttps://bit.ly/stop69', 1),
(26, 'Mike Macduff\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'New Zealand', 'New Zealand', 'If you have a local business and want to rank it on google maps in a specific area then this service is for you. \r\n \r\nGoogle Map Stacking is one of the best ways to rank your GMB in a specific mile radius. \r\n \r\nMore info: \r\nhttps://www.speed-seo.net/product/google-maps-pointers/ \r\n \r\nThanks and Regards \r\nMike Macduff\r\n \r\n \r\nPS: Want an all in one Local Plan that includes everything? \r\nhttps://www.speed-seo.net/product/local-seo-package/', 1),
(27, 'LorenzoSlews', 'lesleyrandle@shaw.ca', 'lesleyrandle@shaw.ca', 'Luxembourg', 'Luxembourg', 'Supercharge Your Website Ranking with 3104 Free Google-Approved Links http://websitetopboost.slushshed.xyz/webtop', 1),
(28, 'Mike Ryder\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'United States', 'United States', 'Hi there \r\n \r\nJust checked your stibuilderslimited.com in MOZ and saw that you could use an authority boost. \r\n \r\nWith our service you will get a guaranteed Domain Authority score within just 3 months time. This will increase the organic visibility and strengthen your website authority, thus getting it stronger against G updates as well. \r\n \r\nFor more information, please check our offers \r\nhttps://www.monkeydigital.co/domain-authority-plan/ \r\n \r\nNEW: Semrush DA is now possible \r\nhttps://www.monkeydigital.co/semrush-da/ \r\n \r\nThanks and regards \r\nMike Ryder\r\n', 1),
(29, 'EdwinMeene', 'scottru@houselink.on.ca', 'scottru@houselink.on.ca', 'Australia', 'Australia', 'Seize the opportunity for financial growth: 10,000 EUR monthly through crypto http://cryptomillionar-6495260.janeshomenews.xyz/anwendung-9559595', 1),
(30, 'Mike Gimson\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'Taiwan', 'Taiwan', 'Howdy \r\n \r\nI have just verified your SEO on  stibuilderslimited.com for the ranking keywords and saw that your website could use a boost. \r\n \r\nWe will improve your ranks organically and safely, using state of the art AI and whitehat methods, while providing monthly reports and outstanding support. \r\n \r\nMore info: \r\nhttps://www.hilkom-digital.de/cheap-seo-packages/ \r\n \r\nRegards \r\nMike Gimson\r\n', 1),
(31, 'Raymondgyday', 'kvtservices@hotmail.ca', 'kvtservices@hotmail.ca', 'United Arab Emirates', 'United Arab Emirates', 'Optimize Your Social Media Campaigns with Elite SMM Services! http://smmstrategieselite-smm-5894547.z-xsmb.com/smmsuccessaccelerator-elite-8979378', 1),
(32, 'Mike Nyman\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'United States', 'United States', 'Hello \r\n \r\nI have just took an in depth look on your  stibuilderslimited.com for onsite errors and saw that your website has a handful of issues which should be addressed. \r\n \r\nNo matter what you are offering or selling, having a poor optimized site, full of bugs and errors, will never help your ranks. \r\n \r\nLet us fix your wordpress site errors today and get your ranks reach their full potential \r\n \r\nMore info: \r\nhttps://www.digital-x-press.com/product/wordpress-seo-audit-and-fix-service/ \r\n \r\n \r\nRegards \r\nMike Nyman\r\n', 1),
(33, 'Mike Gilson\r\n', 'no-replydahorery@gmail.com', 'no-replydahorery@gmail.com', 'Netherlands Antilles', 'Netherlands Antilles', 'Hi \r\n \r\nThis is Mike Gilson\r\n \r\nLet me present you our latest research results from our constant SEO feedbacks that we have from our plans: \r\n \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nThe new Semrush Backlinks, which will make your stibuilderslimited.com SEO trend have an immediate push. \r\nThe method is actually very simple, we are building links from domains that have a high number of keywords ranking for them.  \r\n \r\nForget about the SEO metrics or any other factors that so many tools try to teach you that is good. The most valuable link is the one that comes from a website that has a healthy trend and lots of ranking keywords. \r\nWe thought about that, so we have built this plan for you \r\n \r\nCheck in detail here: \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nCheap and effective \r\n \r\nTry it anytime soon \r\n \r\n \r\nRegards \r\n \r\nMike Gilson\r\n \r\nmike@strictlydigital.net', 1),
(34, 'WilliamHoogy', 'nataliawohler@freesurf.ch', 'nataliawohler@freesurf.ch', 'Sweden', 'Sweden', 'Verdiene Geld im Schlaf – unsere KI-App bringt dir 1000 EUR pro Tag http://autopilot-kiverdienstsystemki.l-kqxs.com/autopilotvermoegen1000eur', 1),
(35, 'Mike Reynolds\r\n', 'mikeFloobe@gmail.com', 'mikeFloobe@gmail.com', 'Netherlands Antilles', 'Netherlands Antilles', 'Hi there, \r\n \r\nMy name is Mike from Monkey Digital, \r\n \r\nAllow me to present to you a lifetime revenue opportunity of 35% \r\nThat\'s right, you can earn 35% of every order made by your affiliate for life. \r\n \r\nSimply register with us, generate your affiliate links, and incorporate them on your website, and you are done. It takes only 5 minutes to set up everything, and the payouts are sent each month. \r\n \r\nClick here to enroll with us today: \r\nhttps://www.monkeydigital.org/affiliate-dashboard/ \r\n \r\nThink about it, \r\nEvery website owner requires the use of search engine optimization (SEO) for their website. This endeavor holds significant potential for both parties involved. \r\n \r\nThanks and regards \r\nMike Reynolds\r\n \r\nMonkey Digital', 1),
(36, 'RandyAniff', 'cbirtch5@sympatico.ca', 'cbirtch5@sympatico.ca', 'Japan', 'Japan', 'CRYPTO FORTUNE ACCELERATOR: MULTIPLY YOUR $100 INVESTMENT INTO $5,000,000 WITH ALTCOINS http://altcoinup.madewinelove.com/cryptowave', 1),
(37, 'RobertDal', 'alfredegov@gmail.com', 'alfredegov@gmail.com', 'United kingdom', 'United kingdom', 'Sveiki, es gribēju zināt savu cenu.', 1),
(38, 'Mike Aldridge\r\n', 'mikedahorery@gmail.com', 'mikedahorery@gmail.com', 'New Zealand', 'New Zealand', 'If you are looking to rank your local business on Google Maps in a specific area, this service is for you. \r\n \r\nGoogle Map Stacking is a highly effective technique for ranking your GMB within a specific mile radius. \r\n \r\nMore info: \r\nhttps://www.speed-seo.net/product/google-maps-pointers/ \r\n \r\nThanks and Regards \r\nMike Aldridge\r\n \r\n \r\nPS: Want a comprehensive local plan that covers everything? \r\nhttps://www.speed-seo.net/product/local-seo-bundle/', 1),
(39, 'BrandonDoosy', 'panic@live.ca', 'panic@live.ca', 'Finland', 'Finland', 'Multiply Your Income Potential: ChatGPT\'s $21,000/Month Passive Income Accelerator http://ads.aquieuropa.com/openx/www/delivery/ck.php?ct=1&oaparams=2__bannerid=259__zoneid=36__OXLCA=1__cb=cd81834d12__oadest=https%3A%2F%2Fonlinshopbest.sell.app%2Fproduct%2Fpassive-income-of-21000-per-month-with-chatgpt-is-easy-money%3F733999555', 1),
(40, 'Hermelinda Gass', 'gass.hermelinda@gmail.com', 'gass.hermelinda@gmail.com', '', '', 'Hi,\r\n\r\nTake back your time—increase conversions by an average of 14x.\r\n \r\nThat’s what This AI can do for your Business or agency.\r\n  \r\nThis Revolutionary AI is a highly trained Artificial Intelligence that:\r\n \r\n- Generates your creatives\r\n- Uses proven design traits\r\n- Makes your life easier\r\n \r\nPlus: New Users get $500 worth of Google Ad Credits for FREE.\r\n \r\nSign up today. Cancel anytime.\r\n \r\nTry 100% free for 7 days  ->  https://bit.ly/431ZvZW \r\n\r\n\r\nCheers!\r\n\r\nAdam Smith\r\n78 Road St, NYC\r\n===============\r\nClick here to Unsubscribe.\r\nhttps://forms.gle/PPk1PGMCJDU2EmX79', 1),
(41, 'RobertDal', 'alfredegov@gmail.com', 'alfredegov@gmail.com', 'France', 'United kingdom', 'Xin chào, tôi muốn biết giá của bạn.', 1),
(42, 'Mike Blare\r\n', 'mikeFloobe@gmail.com', 'mikeFloobe@gmail.com', 'Netherlands Antilles', 'Netherlands Antilles', 'Hi there, \r\n \r\nMy name is Mike from Monkey Digital, \r\n \r\nAllow me to present to you a lifetime revenue opportunity of 35% \r\nThat\'s right, you can earn 35% of every order made by your affiliate for life. \r\n \r\nSimply register with us, generate your affiliate links, and incorporate them on your website, and you are done. It takes only 5 minutes to set up everything, and the payouts are sent each month. \r\n \r\nClick here to enroll with us today: \r\nhttps://www.monkeydigital.org/affiliate-dashboard/ \r\n \r\nThink about it, \r\nEvery website owner requires the use of search engine optimization (SEO) for their website. This endeavor holds significant potential for both parties involved. \r\n \r\nThanks and regards \r\nMike Blare\r\n \r\nMonkey Digital', 1),
(43, 'Jamesruipt', 'chookie0@bigpond.net.au', 'chookie0@bigpond.net.au', 'France', 'France', 'Your Path to Financial Abundance: $1000 a Day on Google http://sidehustle.lottovip888.xyz/hustletime', 1),
(44, 'Michalak Aleksandra', 'wmueller831@gmail.com', 'wmueller831@gmail.com', 'Germany', 'Germany', 'Hello, \r\nHow are you doing? My name is Mr Michalak Aleksandra, and I am a financial consultant. I am reaching out to you today to offer my expertise, experience, and network of investors to assist you in achieving your business goals. \r\nWe are a financial consulting firm and we have reputable investors that are expanding their global presence by investing in viable projects across the globe. They are willing to Invest from $1,000,000 and above in viable project(s) at 3% ROI per annum for 1-10 years and 12 months moratorium. \r\nIf you have viable projects that need funding, kindly send your business plan/executive summary for our review and possible funding. \r\nIf you are interested in any of the above, kindly respond to us via this email \r\nmichalakaleksandrama@gmail.com I wait to hear from you. \r\nRegards, \r\nMichalak Aleksandra \r\nE-mail: michalakaleksandrama@gmail.com', 1),
(45, 'HermanTauri', 'margarita.cabellon@bridgeleader.com', 'margarita.cabellon@bridgeleader.com', 'Germany', 'Germany', 'CAPTURE THE BITCOIN OPPORTUNITY: GET A WALLET FILE WITH 12600 BTC http://quickfortunes.digitaleyecare.xyz/btcjumpstartnow', 1),
(46, 'Mike Albertson\r\n', 'mikesifable@gmail.com', 'mikesifable@gmail.com', 'Taiwan', 'Taiwan', 'Hi there \r\n \r\nJust checked your stibuilderslimited.com backlink profile, I noticed a moderate percentage of toxic links pointing to your website \r\n \r\nWe will investigate each link for its toxicity and perform a professional clean up for you free of charge. \r\n \r\nStart recovering your ranks today: \r\nhttps://www.hilkom-digital.de/professional-linksprofile-clean-up-service/ \r\n \r\n \r\nRegards \r\nMike Albertson\r\nHilkom Digital SEO Experts \r\nhttps://www.hilkom-digital.de/', 1),
(47, 'Mike Erickson\r\n', 'mikesifable@gmail.com', 'mikesifable@gmail.com', 'United States', 'United States', 'Hi there, \r\n \r\nI have reviewed your domain in MOZ and have observed that you may benefit from an increase in authority. \r\n \r\nOur solution guarantees you a high-quality domain authority score within a period of three months. This will increase your organic visibility and strengthen your website authority, thus making it stronger against Google updates. \r\n \r\nCheck out our deals for more details. \r\nhttps://www.monkeydigital.co/domain-authority-plan/ \r\n \r\nNEW: Ahrefs Domain Rating \r\nhttps://www.monkeydigital.co/ahrefs-seo/ \r\n \r\nThanks and regards \r\nMike Erickson\r\n', 1),
(48, 'Peter Miln\r\n', 'peterquenteeVet@gmail.com', 'peterquenteeVet@gmail.com', 'United States', 'United States', 'Hi there \r\n \r\nWhat if you could grab all the possible resources that your competitors rank with. \r\n \r\nOur competition search strategy will examine tens of millions of backlinks to find available resources that all your major rivals possess, and then use them to your advantage. \r\n \r\nGet your site to the top of the search results with a cutting-edge plan. \r\n \r\nMore info: \r\nhttps://www.digital-x-press.com/product/competition-seo-plan/ \r\n \r\n \r\nPeter Miln\r\nDigital X Press SEO Agency \r\nhttps://www.digital-x-press.com/', 1),
(49, 'Danielgeazy', 'frenvhy@yahoo.com', 'frenvhy@yahoo.com', 'Netherlands', 'Netherlands', 'BUY NOW BITCOIN WALLET WITH 12600 BTC ON YOUR BALANCE - 3 DAYS LEFT http://getBTC12600now.randiesiegellaw.com/BTC12600prize', 1),
(50, 'Mike Duncan\r\n', 'mikedahorery@gmail.com', 'mikedahorery@gmail.com', 'Netherlands Antilles', 'Netherlands Antilles', 'Hi there \r\n \r\nThis is Mike Duncan\r\n \r\nLet me present you our latest research results from our constant SEO feedbacks that we have from our plans: \r\n \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nThe new Semrush Backlinks, which will make your stibuilderslimited.com SEO trend have an immediate push. \r\nThe method is actually very simple, we are building links from domains that have a high number of keywords ranking for them.  \r\n \r\nForget about the SEO metrics or any other factors that so many tools try to teach you that is good. The most valuable link is the one that comes from a website that has a healthy trend and lots of ranking keywords. \r\nWe thought about that, so we have built this plan for you \r\n \r\nCheck in detail here: \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nCheap and effective \r\n \r\nTry it anytime soon \r\n \r\n \r\nRegards \r\n \r\nMike Duncan\r\n \r\nmike@strictlydigital.net', 1),
(51, 'RobertDal', 'alfredegov@gmail.com', 'alfredegov@gmail.com', 'Georgia', 'United kingdom', 'Hi, ego volo scire vestri pretium.', 1),
(52, 'Milla Carboni', 'carboni.milla@gmail.com', 'carboni.milla@gmail.com', '', '', 'Hey there, I just found your site, quick question…\r\n\r\nI found stibuilderslimited.com after doing a quick search – you showed up near the top of the rankings, so whatever you’re doing for SEO, looks like it’s working well.\r\n\r\nSo here’s my question – what happens AFTER someone lands on your site?  Anything?\r\n\r\nResearch tells us at least 70% of the people who find your site, after a quick once-over, they disappear… forever.\r\n\r\nThat means that all the work and effort you put into getting them to show up, goes down the tubes.\r\n\r\nWhy would you want all that good work – and the great site you’ve built – go to waste?\r\n\r\nBecause the odds are they’ll just skip over calling or even grabbing their phone, leaving you high and dry.\r\n\r\nBut here’s a thought… what if you could make it super-simple for someone to raise their hand, say, “okay, let’s talk” without requiring them to even pull their cell phone from their pocket?\r\n  \r\nYou can – thanks to revolutionary new software that can literally make that first call happen NOW.\r\n\r\nTurboLeadGeneration.com is a software widget that sits on your site, ready and waiting to capture any visitor’s Name, Email address and Phone Number.  It lets you know IMMEDIATELY – so that you can talk to that lead while they’re still there at your site.\r\n  \r\nYou know, strike when the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to try out a Live Demo with Talk With Web Visitor now to see exactly how it works.\r\n\r\nWhen targeting leads, you HAVE to act fast – the difference between contacting someone within 5 minutes versus 30 minutes later is huge – like 100 times better!\r\n\r\nThat’s why you should check out our new SMS Text With Lead feature as well… once you’ve captured the phone number of the website visitor, you can automatically kick off a text message (SMS) conversation with them. \r\n \r\nImagine how powerful this could be – even if they don’t take you up on your offer immediately, you can stay in touch with them using text messages to make new offers, provide links to great content, and build your credibility.\r\n\r\nJust this alone could be a game changer to make your website even more effective.\r\n\r\nStrike when  the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to learn more about everything Talk With Web Visitor can do for your business – you’ll be amazed.\r\n\r\nThanks and keep up the great work!\r\n\r\nPS: TurboLeadGeneration.com offers a FREE 14 days trial – you could be converting up to 100x more leads immediately!   \r\nIt even includes International Long Distance Calling. \r\nStop wasting money chasing eyeballs that don’t turn into paying customers. \r\nCLICK HERE https://TurboLeadGeneration.com to try Talk With Web Visitor now.\r\n\r\nIf you\'d like to unsubscribe click here http://TurboLeadGeneration.com/unsubscribe.aspx?d=stibuilderslimited.com', 1),
(53, 'Tristan Jasper', 'jasper.tristan@gmail.com', 'jasper.tristan@gmail.com', '', '', 'Hey there, I just found your site, quick question…\r\n\r\nI found stibuilderslimited.com after doing a quick search – you showed up near the top of the rankings, so whatever you’re doing for SEO, looks like it’s working well.\r\n\r\nSo here’s my question – what happens AFTER someone lands on your site?  Anything?\r\n\r\nResearch tells us at least 70% of the people who find your site, after a quick once-over, they disappear… forever.\r\n\r\nThat means that all the work and effort you put into getting them to show up, goes down the tubes.\r\n\r\nWhy would you want all that good work – and the great site you’ve built – go to waste?\r\n\r\nBecause the odds are they’ll just skip over calling or even grabbing their phone, leaving you high and dry.\r\n\r\nBut here’s a thought… what if you could make it super-simple for someone to raise their hand, say, “okay, let’s talk” without requiring them to even pull their cell phone from their pocket?\r\n  \r\nYou can – thanks to revolutionary new software that can literally make that first call happen NOW.\r\n\r\nTurboLeadGeneration.com is a software widget that sits on your site, ready and waiting to capture any visitor’s Name, Email address and Phone Number.  It lets you know IMMEDIATELY – so that you can talk to that lead while they’re still there at your site.\r\n  \r\nYou know, strike when the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to try out a Live Demo with Talk With Web Visitor now to see exactly how it works.\r\n\r\nWhen targeting leads, you HAVE to act fast – the difference between contacting someone within 5 minutes versus 30 minutes later is huge – like 100 times better!\r\n\r\nThat’s why you should check out our new SMS Text With Lead feature as well… once you’ve captured the phone number of the website visitor, you can automatically kick off a text message (SMS) conversation with them. \r\n \r\nImagine how powerful this could be – even if they don’t take you up on your offer immediately, you can stay in touch with them using text messages to make new offers, provide links to great content, and build your credibility.\r\n\r\nJust this alone could be a game changer to make your website even more effective.\r\n\r\nStrike when  the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to learn more about everything Talk With Web Visitor can do for your business – you’ll be amazed.\r\n\r\nThanks and keep up the great work!\r\n\r\nPS: TurboLeadGeneration.com offers a FREE 14 days trial – you could be converting up to 100x more leads immediately!   \r\nIt even includes International Long Distance Calling. \r\nStop wasting money chasing eyeballs that don’t turn into paying customers. \r\nCLICK HERE https://TurboLeadGeneration.com to try Talk With Web Visitor now.\r\n\r\nIf you\'d like to unsubscribe click here http://TurboLeadGeneration.com/unsubscribe.aspx?d=stibuilderslimited.com', 1),
(54, 'Bah Mbi', 'bahmbi129@gmail.com', 'bahmbi129@gmail.com', 'Kuwait', 'Kuwait', 'Attn. Director, \r\n \r\nWe are interested in your products. Please contact us with your product details and price list if your company can handle a bulk supply of your products to Cameroon. \r\nPlease send your reply to bahmbim3@oiedcadmin.org \r\n \r\nHRM Bah Mbi', 1),
(55, 'RobertDal', 'alfredegov@gmail.com', 'alfredegov@gmail.com', 'Georgia', 'France', 'Ողջույն, ես ուզում էի իմանալ ձեր գինը.', 1),
(56, 'Mike Barrington\r\n', 'mikedahorery@gmail.com', 'mikedahorery@gmail.com', 'New Zealand', 'New Zealand', 'If you are looking to rank your local business on Google Maps in a specific area, this service is for you. \r\n \r\nGoogle Map Stacking is a highly effective technique for ranking your GMB within a specific mile radius. \r\n \r\nMore info: \r\nhttps://www.speed-seo.net/product/google-maps-pointers/ \r\n \r\nThanks and Regards \r\nMike Barrington\r\n \r\n \r\nPS: Want a comprehensive local plan that covers everything? \r\nhttps://www.speed-seo.net/product/local-seo-bundle/', 1),
(57, 'Donte Borden', 'donte.borden@outlook.com', 'donte.borden@outlook.com', '', '', 'Hey there, I just found your site, quick question…\r\n\r\nI found stibuilderslimited.com after doing a quick search – you showed up near the top of the rankings, so whatever you’re doing for SEO, looks like it’s working well.\r\n\r\nSo here’s my question – what happens AFTER someone lands on your site?  Anything?\r\n\r\nResearch tells us at least 70% of the people who find your site, after a quick once-over, they disappear… forever.\r\n\r\nThat means that all the work and effort you put into getting them to show up, goes down the tubes.\r\n\r\nWhy would you want all that good work – and the great site you’ve built – go to waste?\r\n\r\nBecause the odds are they’ll just skip over calling or even grabbing their phone, leaving you high and dry.\r\n\r\nBut here’s a thought… what if you could make it super-simple for someone to raise their hand, say, “okay, let’s talk” without requiring them to even pull their cell phone from their pocket?\r\n  \r\nYou can – thanks to revolutionary new software that can literally make that first call happen NOW.\r\n\r\nTurboLeadGeneration.com is a software widget that sits on your site, ready and waiting to capture any visitor’s Name, Email address and Phone Number.  It lets you know IMMEDIATELY – so that you can talk to that lead while they’re still there at your site.\r\n  \r\nYou know, strike when the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to try out a Live Demo with Talk With Web Visitor now to see exactly how it works.\r\n\r\nWhen targeting leads, you HAVE to act fast – the difference between contacting someone within 5 minutes versus 30 minutes later is huge – like 100 times better!\r\n\r\nThat’s why you should check out our new SMS Text With Lead feature as well… once you’ve captured the phone number of the website visitor, you can automatically kick off a text message (SMS) conversation with them. \r\n \r\nImagine how powerful this could be – even if they don’t take you up on your offer immediately, you can stay in touch with them using text messages to make new offers, provide links to great content, and build your credibility.\r\n\r\nJust this alone could be a game changer to make your website even more effective.\r\n\r\nStrike when  the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to learn more about everything Talk With Web Visitor can do for your business – you’ll be amazed.\r\n\r\nThanks and keep up the great work!\r\n\r\nPS: TurboLeadGeneration.com offers a FREE 14 days trial – you could be converting up to 100x more leads immediately!   \r\nIt even includes International Long Distance Calling. \r\nStop wasting money chasing eyeballs that don’t turn into paying customers. \r\nCLICK HERE https://TurboLeadGeneration.com to try Talk With Web Visitor now.\r\n\r\nIf you\'d like to unsubscribe click here http://TurboLeadGeneration.com/unsubscribe.aspx?d=stibuilderslimited.com', 1),
(58, 'Richard Bucher', 'bucher.richard@googlemail.com', 'bucher.richard@googlemail.com', '', '', 'Hey there, I just found your site, quick question…\r\n\r\nI found stibuilderslimited.com after doing a quick search – you showed up near the top of the rankings, so whatever you’re doing for SEO, looks like it’s working well.\r\n\r\nSo here’s my question – what happens AFTER someone lands on your site?  Anything?\r\n\r\nResearch tells us at least 70% of the people who find your site, after a quick once-over, they disappear… forever.\r\n\r\nThat means that all the work and effort you put into getting them to show up, goes down the tubes.\r\n\r\nWhy would you want all that good work – and the great site you’ve built – go to waste?\r\n\r\nBecause the odds are they’ll just skip over calling or even grabbing their phone, leaving you high and dry.\r\n\r\nBut here’s a thought… what if you could make it super-simple for someone to raise their hand, say, “okay, let’s talk” without requiring them to even pull their cell phone from their pocket?\r\n  \r\nYou can – thanks to revolutionary new software that can literally make that first call happen NOW.\r\n\r\nTurboLeadGeneration.com is a software widget that sits on your site, ready and waiting to capture any visitor’s Name, Email address and Phone Number.  It lets you know IMMEDIATELY – so that you can talk to that lead while they’re still there at your site.\r\n  \r\nYou know, strike when the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to try out a Live Demo with Talk With Web Visitor now to see exactly how it works.\r\n\r\nWhen targeting leads, you HAVE to act fast – the difference between contacting someone within 5 minutes versus 30 minutes later is huge – like 100 times better!\r\n\r\nThat’s why you should check out our new SMS Text With Lead feature as well… once you’ve captured the phone number of the website visitor, you can automatically kick off a text message (SMS) conversation with them. \r\n \r\nImagine how powerful this could be – even if they don’t take you up on your offer immediately, you can stay in touch with them using text messages to make new offers, provide links to great content, and build your credibility.\r\n\r\nJust this alone could be a game changer to make your website even more effective.\r\n\r\nStrike when  the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to learn more about everything Talk With Web Visitor can do for your business – you’ll be amazed.\r\n\r\nThanks and keep up the great work!\r\n\r\nPS: TurboLeadGeneration.com offers a FREE 14 days trial – you could be converting up to 100x more leads immediately!   \r\nIt even includes International Long Distance Calling. \r\nStop wasting money chasing eyeballs that don’t turn into paying customers. \r\nCLICK HERE https://TurboLeadGeneration.com to try Talk With Web Visitor now.\r\n\r\nIf you\'d like to unsubscribe click here http://TurboLeadGeneration.com/unsubscribe.aspx?d=stibuilderslimited.com', 1);
INSERT INTO `realstateapp_contactmessage` (`id`, `name`, `email`, `property_plot_type`, `location`, `apartment_size`, `message`, `status`) VALUES
(59, 'Keisha Kaestner', 'keisha.kaestner@gmail.com', 'keisha.kaestner@gmail.com', '', '', 'Hey there, I just found your site, quick question…\r\n\r\nI found stibuilderslimited.com after doing a quick search – you showed up near the top of the rankings, so whatever you’re doing for SEO, looks like it’s working well.\r\n\r\nSo here’s my question – what happens AFTER someone lands on your site?  Anything?\r\n\r\nResearch tells us at least 70% of the people who find your site, after a quick once-over, they disappear… forever.\r\n\r\nThat means that all the work and effort you put into getting them to show up, goes down the tubes.\r\n\r\nWhy would you want all that good work – and the great site you’ve built – go to waste?\r\n\r\nBecause the odds are they’ll just skip over calling or even grabbing their phone, leaving you high and dry.\r\n\r\nBut here’s a thought… what if you could make it super-simple for someone to raise their hand, say, “okay, let’s talk” without requiring them to even pull their cell phone from their pocket?\r\n  \r\nYou can – thanks to revolutionary new software that can literally make that first call happen NOW.\r\n\r\nTurboLeadGeneration.com is a software widget that sits on your site, ready and waiting to capture any visitor’s Name, Email address and Phone Number.  It lets you know IMMEDIATELY – so that you can talk to that lead while they’re still there at your site.\r\n  \r\nYou know, strike when the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to try out a Live Demo with Talk With Web Visitor now to see exactly how it works.\r\n\r\nWhen targeting leads, you HAVE to act fast – the difference between contacting someone within 5 minutes versus 30 minutes later is huge – like 100 times better!\r\n\r\nThat’s why you should check out our new SMS Text With Lead feature as well… once you’ve captured the phone number of the website visitor, you can automatically kick off a text message (SMS) conversation with them. \r\n \r\nImagine how powerful this could be – even if they don’t take you up on your offer immediately, you can stay in touch with them using text messages to make new offers, provide links to great content, and build your credibility.\r\n\r\nJust this alone could be a game changer to make your website even more effective.\r\n\r\nStrike when  the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to learn more about everything Talk With Web Visitor can do for your business – you’ll be amazed.\r\n\r\nThanks and keep up the great work!\r\n\r\nPS: TurboLeadGeneration.com offers a FREE 14 days trial – you could be converting up to 100x more leads immediately!   \r\nIt even includes International Long Distance Calling. \r\nStop wasting money chasing eyeballs that don’t turn into paying customers. \r\nCLICK HERE https://TurboLeadGeneration.com to try Talk With Web Visitor now.\r\n\r\nIf you\'d like to unsubscribe click here http://TurboLeadGeneration.com/unsubscribe.aspx?d=stibuilderslimited.com', 1),
(60, 'Vern Farrelly', 'farrelly.vern@outlook.com', 'farrelly.vern@outlook.com', '', '', 'Hey there, I just found your site, quick question…\r\n\r\nI found stibuilderslimited.com after doing a quick search – you showed up near the top of the rankings, so whatever you’re doing for SEO, looks like it’s working well.\r\n\r\nSo here’s my question – what happens AFTER someone lands on your site?  Anything?\r\n\r\nResearch tells us at least 70% of the people who find your site, after a quick once-over, they disappear… forever.\r\n\r\nThat means that all the work and effort you put into getting them to show up, goes down the tubes.\r\n\r\nWhy would you want all that good work – and the great site you’ve built – go to waste?\r\n\r\nBecause the odds are they’ll just skip over calling or even grabbing their phone, leaving you high and dry.\r\n\r\nBut here’s a thought… what if you could make it super-simple for someone to raise their hand, say, “okay, let’s talk” without requiring them to even pull their cell phone from their pocket?\r\n  \r\nYou can – thanks to revolutionary new software that can literally make that first call happen NOW.\r\n\r\nTurboLeadGeneration.com is a software widget that sits on your site, ready and waiting to capture any visitor’s Name, Email address and Phone Number.  It lets you know IMMEDIATELY – so that you can talk to that lead while they’re still there at your site.\r\n  \r\nYou know, strike when the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to try out a Live Demo with Talk With Web Visitor now to see exactly how it works.\r\n\r\nWhen targeting leads, you HAVE to act fast – the difference between contacting someone within 5 minutes versus 30 minutes later is huge – like 100 times better!\r\n\r\nThat’s why you should check out our new SMS Text With Lead feature as well… once you’ve captured the phone number of the website visitor, you can automatically kick off a text message (SMS) conversation with them. \r\n \r\nImagine how powerful this could be – even if they don’t take you up on your offer immediately, you can stay in touch with them using text messages to make new offers, provide links to great content, and build your credibility.\r\n\r\nJust this alone could be a game changer to make your website even more effective.\r\n\r\nStrike when  the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to learn more about everything Talk With Web Visitor can do for your business – you’ll be amazed.\r\n\r\nThanks and keep up the great work!\r\n\r\nPS: TurboLeadGeneration.com offers a FREE 14 days trial – you could be converting up to 100x more leads immediately!   \r\nIt even includes International Long Distance Calling. \r\nStop wasting money chasing eyeballs that don’t turn into paying customers. \r\nCLICK HERE https://TurboLeadGeneration.com to try Talk With Web Visitor now.\r\n\r\nIf you\'d like to unsubscribe click here http://TurboLeadGeneration.com/unsubscribe.aspx?d=stibuilderslimited.com', 1),
(61, 'Esther Niall', 'esther.niall@gmail.com', 'esther.niall@gmail.com', '', '', 'Hey there, I just found your site, quick question…\r\n\r\nI found stibuilderslimited.com after doing a quick search – you showed up near the top of the rankings, so whatever you’re doing for SEO, looks like it’s working well.\r\n\r\nSo here’s my question – what happens AFTER someone lands on your site?  Anything?\r\n\r\nResearch tells us at least 70% of the people who find your site, after a quick once-over, they disappear… forever.\r\n\r\nThat means that all the work and effort you put into getting them to show up, goes down the tubes.\r\n\r\nWhy would you want all that good work – and the great site you’ve built – go to waste?\r\n\r\nBecause the odds are they’ll just skip over calling or even grabbing their phone, leaving you high and dry.\r\n\r\nBut here’s a thought… what if you could make it super-simple for someone to raise their hand, say, “okay, let’s talk” without requiring them to even pull their cell phone from their pocket?\r\n  \r\nYou can – thanks to revolutionary new software that can literally make that first call happen NOW.\r\n\r\nTurboLeadGeneration.com is a software widget that sits on your site, ready and waiting to capture any visitor’s Name, Email address and Phone Number.  It lets you know IMMEDIATELY – so that you can talk to that lead while they’re still there at your site.\r\n  \r\nYou know, strike when the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to try out a Live Demo with Talk With Web Visitor now to see exactly how it works.\r\n\r\nWhen targeting leads, you HAVE to act fast – the difference between contacting someone within 5 minutes versus 30 minutes later is huge – like 100 times better!\r\n\r\nThat’s why you should check out our new SMS Text With Lead feature as well… once you’ve captured the phone number of the website visitor, you can automatically kick off a text message (SMS) conversation with them. \r\n \r\nImagine how powerful this could be – even if they don’t take you up on your offer immediately, you can stay in touch with them using text messages to make new offers, provide links to great content, and build your credibility.\r\n\r\nJust this alone could be a game changer to make your website even more effective.\r\n\r\nStrike when  the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to learn more about everything Talk With Web Visitor can do for your business – you’ll be amazed.\r\n\r\nThanks and keep up the great work!\r\n\r\nPS: TurboLeadGeneration.com offers a FREE 14 days trial – you could be converting up to 100x more leads immediately!   \r\nIt even includes International Long Distance Calling. \r\nStop wasting money chasing eyeballs that don’t turn into paying customers. \r\nCLICK HERE https://TurboLeadGeneration.com to try Talk With Web Visitor now.\r\n\r\nIf you\'d like to unsubscribe click here http://TurboLeadGeneration.com/unsubscribe.aspx?d=stibuilderslimited.com', 1),
(62, 'Hanna Miner', 'hanna.miner48@gmail.com', 'hanna.miner48@gmail.com', '', '', 'Hey there, I just found your site, quick question…\r\n\r\nI found stibuilderslimited.com after doing a quick search – you showed up near the top of the rankings, so whatever you’re doing for SEO, looks like it’s working well.\r\n\r\nSo here’s my question – what happens AFTER someone lands on your site?  Anything?\r\n\r\nResearch tells us at least 70% of the people who find your site, after a quick once-over, they disappear… forever.\r\n\r\nThat means that all the work and effort you put into getting them to show up, goes down the tubes.\r\n\r\nWhy would you want all that good work – and the great site you’ve built – go to waste?\r\n\r\nBecause the odds are they’ll just skip over calling or even grabbing their phone, leaving you high and dry.\r\n\r\nBut here’s a thought… what if you could make it super-simple for someone to raise their hand, say, “okay, let’s talk” without requiring them to even pull their cell phone from their pocket?\r\n  \r\nYou can – thanks to revolutionary new software that can literally make that first call happen NOW.\r\n\r\nTurboLeadGeneration.com is a software widget that sits on your site, ready and waiting to capture any visitor’s Name, Email address and Phone Number.  It lets you know IMMEDIATELY – so that you can talk to that lead while they’re still there at your site.\r\n  \r\nYou know, strike when the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to try out a Live Demo with Talk With Web Visitor now to see exactly how it works.\r\n\r\nWhen targeting leads, you HAVE to act fast – the difference between contacting someone within 5 minutes versus 30 minutes later is huge – like 100 times better!\r\n\r\nThat’s why you should check out our new SMS Text With Lead feature as well… once you’ve captured the phone number of the website visitor, you can automatically kick off a text message (SMS) conversation with them. \r\n \r\nImagine how powerful this could be – even if they don’t take you up on your offer immediately, you can stay in touch with them using text messages to make new offers, provide links to great content, and build your credibility.\r\n\r\nJust this alone could be a game changer to make your website even more effective.\r\n\r\nStrike when  the iron’s hot!\r\n\r\nCLICK HERE https://TurboLeadGeneration.com to learn more about everything Talk With Web Visitor can do for your business – you’ll be amazed.\r\n\r\nThanks and keep up the great work!\r\n\r\nPS: TurboLeadGeneration.com offers a FREE 14 days trial – you could be converting up to 100x more leads immediately!   \r\nIt even includes International Long Distance Calling. \r\nStop wasting money chasing eyeballs that don’t turn into paying customers. \r\nCLICK HERE https://TurboLeadGeneration.com to try Talk With Web Visitor now.\r\n\r\nIf you\'d like to unsubscribe click here http://TurboLeadGeneration.com/unsubscribe.aspx?d=stibuilderslimited.com', 1),
(63, 'Josephseato', 'no.reply.JozefDupont@gmail.com', 'no.reply.JozefDupont@gmail.com', 'Nicaragua', 'Nicaragua', 'What’s up? stibuilderslimited.com \r\n \r\nDid you know that it is possible to send commercial offer legally? We propose a way of sending commercial offers through feedback forms. You can find these feedback forms on a lot of sites. \r\nWhen such requests are sent, no personal data is used, and messages are sent to forms specifically designed to receive messages and appeals securely. Feedback Forms guarantee that messages won\'t be marked as spam, since they are considered important. \r\nYou can now take advantage of our service free of charge. \r\nWe are able to provide up to 50,000 messages for you. \r\n \r\nThe cost of sending one million messages is $59. \r\n \r\nThis letter is automatically generated. \r\nPlease use the contact details below to get in touch with us. \r\n \r\nContact us. \r\nTelegram - https://t.me/FeedbackFormEU \r\nSkype  live:feedbackform2019 \r\nWhatsApp  +375259112693 \r\nWhatsApp  https://wa.me/+375259112693 \r\n \r\nWe only use chat for communication.', 1),
(64, 'Mike Little\r\n', 'mikesifable@gmail.com', 'mikesifable@gmail.com', 'United States', 'United States', 'Hi there, \r\n \r\nI have reviewed your domain in MOZ and have observed that you may benefit from an increase in authority. \r\n \r\nOur solution guarantees you a high-quality domain authority score within a period of three months. This will increase your organic visibility and strengthen your website authority, thus making it stronger against Google updates. \r\n \r\nCheck out our deals for more details. \r\nhttps://www.monkeydigital.co/domain-authority-plan/ \r\n \r\nNEW: Ahrefs Domain Rating \r\nhttps://www.monkeydigital.co/ahrefs-seo/ \r\n \r\nThanks and regards \r\nMike Little\r\n', 1),
(65, 'Mike Hawkins\r\n', 'mikesifable@gmail.com', 'mikesifable@gmail.com', 'Taiwan', 'Taiwan', 'Hi there \r\n \r\nJust checked your stibuilderslimited.com baclink profile, I noticed a moderate percentage of toxic links pointing to your website \r\n \r\nWe will investigate each link for its toxicity and perform a professional clean up for you free of charge. \r\n \r\nStart recovering your ranks today: \r\nhttps://www.hilkom-digital.de/professional-linksprofile-clean-up-service/ \r\n \r\n \r\nRegards \r\nMike Hawkins\r\nHilkom Digital SEO Experts \r\nhttps://www.hilkom-digital.de/', 1),
(66, 'RobertDal', 'alfredegov@gmail.com', 'alfredegov@gmail.com', 'United kingdom', 'Germany', 'Hæ, ég vildi vita verð þitt.', 1),
(67, 'Mike Benson\r\n', 'peterquenteeVet@gmail.com', 'peterquenteeVet@gmail.com', 'United States', 'United States', 'Hi \r\n \r\nI have just verified your SEO on  stibuilderslimited.com for its SEO Trend and saw that your website could use a boost. \r\n \r\nWe will improve your ranks organically and safely, using only state of the art AI and whitehat methods, while providing monthly reports and outstanding support. \r\n \r\nMore info: \r\nhttps://www.digital-x-press.com/unbeatable-seo/ \r\n \r\n \r\nRegards \r\nMike Benson\r\nDigital X SEO Experts', 1),
(68, 'TimothySteab', 'yasen.krasen.13+93708@mail.ru', 'yasen.krasen.13+93708@mail.ru', 'Spain', 'Spain', 'Mfhfujfehfueh ifwjifjeighufijsdh uidfsjkdokwefuhgedjij idoweweureiurioweiidkjsdj iwjdsksosjfeihfiwskdoakd ijwdiwdowjfihefiwjdiwhfgue stibuilderslimited.com', 1),
(69, 'GregoryEscat', 'florencia_lynch@hotmail.com', 'florencia_lynch@hotmail.com', 'Australia', 'Australia', 'HOW TO EASILY AND SIMPLY MAKE CHATGPT BRING YOU PASSIVE INCOME FROM $1000 PER DAY http://ai-6371.ketlenpack.online/exclusive', 1),
(70, 'Mike Goldman\r\n', 'mikedahorery@gmail.com', 'mikedahorery@gmail.com', 'Netherlands Antilles', 'Netherlands Antilles', 'Good Day \r\n \r\nThis is Mike Goldman\r\n \r\nLet me introduce to you our latest research results from our constant SEO feedbacks that we have from our plans: \r\n \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nThe new Semrush Backlinks, which will make your stibuilderslimited.com SEO trend have an immediate push. \r\nThe method is actually very simple, we are building links from domains that have a high number of keywords ranking for them.  \r\n \r\nForget about the SEO metrics or any other factors that so many tools try to teach you that is good. The most valuable link is the one that comes from a website that has a healthy trend and lots of ranking keywords. \r\nWe thought about that, so we have built this plan for you \r\n \r\nCheck in detail here: \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nCheap and effective \r\n \r\nTry it anytime soon \r\n \r\n \r\nRegards \r\n \r\nMike Goldman\r\n \r\nmike@strictlydigital.net', 1),
(71, 'Mike Nash\r\n', 'mikedahorery@gmail.com', 'mikedahorery@gmail.com', 'New Zealand', 'New Zealand', 'If you are looking to rank your local business on Google Maps in a specific area, this service is for you. \r\n \r\nGoogle Map Stacking is a highly effective technique for ranking your GMB within a specific mile radius. \r\n \r\nMore info: \r\nhttps://www.speed-seo.net/product/google-maps-pointers/ \r\n \r\nThanks and Regards \r\nMike Nash\r\n \r\n \r\nPS: Want a comprehensive local plan that covers everything? \r\nhttps://www.speed-seo.net/product/local-seo-bundle/', 1),
(72, 'DouglasAngen', 'kobadavid@gmail.com', 'kobadavid@gmail.com', 'United Kingdom', 'United Kingdom', 'Make Your First $100,000 Forex Trading http://forex-5221.myparisevents.com/invite', 1),
(73, 'RobertDal', 'alfredegov@gmail.com', 'alfredegov@gmail.com', 'Poland', 'Germany', 'Salam, qiymətinizi bilmək istədim.', 1),
(74, 'DouglasAngen', 'annmariedonoghue@hotmail.com', 'annmariedonoghue@hotmail.com', 'United Kingdom', 'United Kingdom', 'TODAY YOU WILL RECEIVE A TRANSFER OF $100,000, TAKE IT RIGHT NOW http://forex-9392.elisou.com/product', 1),
(75, 'Mike Dean\r\n', 'mikesifable@gmail.com', 'mikesifable@gmail.com', 'Taiwan', 'Taiwan', 'Hi there \r\n \r\nJust checked your stibuilderslimited.com baclink profile, I noticed a moderate percentage of toxic links pointing to your website \r\n \r\nWe will investigate each link for its toxicity and perform a professional clean up for you free of charge. \r\n \r\nStart recovering your ranks today: \r\nhttps://www.hilkom-digital.de/professional-linksprofile-clean-up-service/ \r\n \r\n \r\nRegards \r\nMike Dean\r\nHilkom Digital SEO Experts \r\nhttps://www.hilkom-digital.de/', 1),
(76, 'Mike Molligan\r\n', 'mikesifable@gmail.com', 'mikesifable@gmail.com', 'United States', 'United States', 'Hi there, \r\n \r\nI have reviewed your domain in MOZ and have observed that you may benefit from an increase in authority. \r\n \r\nOur solution guarantees you a high-quality domain authority score within a period of three months. This will increase your organic visibility and strengthen your website authority, thus making it stronger against Google updates. \r\n \r\nCheck out our deals for more details. \r\nhttps://www.monkeydigital.co/domain-authority-plan/ \r\n \r\nNEW: Ahrefs Domain Rating \r\nhttps://www.monkeydigital.co/ahrefs-seo/ \r\n \r\nThanks and regards \r\nMike Molligan\r\n', 1),
(77, 'Dir. Chewn', 'dir.chau0090@gmail.com', 'dir.chau0090@gmail.com', 'Austria', 'Austria', 'Greetings, \r\n \r\nI have an exciting business opportunity to discuss with you. Your prompt response is highly appreciated. Please reply to this email address: changdir80@gmail.com. I will only respond to messages sent to this email. changdir80@gmail.com. \r\n \r\nThank you. \r\n \r\nSincerely, \r\nDir. Chewn', 1),
(78, 'Diana Kelsey', 'diana.kelsey@tutanota.com', 'diana.kelsey@tutanota.com', 'United Kingdom', 'United Kingdom', 'Hello \r\n \r\nI was browsing your website but couldn\'t find any contact information for your Export department. \r\nCould you please forward my email to them? We are currently seeking new suppliers. \r\n \r\nLet me provide a brief introduction about us: \r\nMy name is Mrs. Diana Kelsey and I am representing a reputable company called UK Kingfisher PLC. \r\nKingfisher PLC is a well-known international home improvement company with more than 1,500 stores. \r\nOur operations span across eight countries in Europe. \r\n \r\nKind Regards \r\n \r\nDiana Kelsey \r\n \r\nSenior Executive Purchase \r\n \r\nKingfisher PLC \r\n3 Sheldon Square,London \r\nUnited Kingdom \r\nW2 6PX \r\nPhone: +44 7423 169656 \r\nEmail: purchasing@kingfishersplc.com', 1),
(79, 'Eric Jones', 'ericjonesmyemail@gmail.com', 'ericjonesmyemail@gmail.com', '', '', 'To the\r\n\r\nMy name’s Eric and I just found your site stibuilderslimited.com.\r\n\r\nIt’s got a lot going for it, but here’s an idea to make it even MORE effective.\r\n\r\nCLICK HERE https://advanceleadgeneration.com for a live demo now.\r\n\r\nWeb Visitors Into Leads is a software widget that’s works on your site, ready to capture any visitor’s Name, Email address and Phone Number.  It signals you the moment they let you know they’re interested – so that you can talk to that lead while they’re literally looking over your site.\r\n\r\nAnd once you’ve captured their phone number, with our new SMS Text With Lead feature, you can automatically start a text (SMS) conversation… and if they don’t take you up on your offer then, you can follow up with text messages for new offers, content links, even just “how you doing?” notes to build a relationship.\r\n\r\nCLICK HERE https://advanceleadgeneration.com to discover what Web Visitors Into Leads can do for your business.\r\n\r\nThe difference between contacting someone within 5 minutes versus a half-hour means you could be converting up to 100X more leads today!\r\n\r\nEric\r\nPS: Studies show that 70% of a site’s visitors disappear and are gone forever after just a moment. Don’t keep losing them. \r\nWeb Visitors Into Leads offers a FREE 14 days trial – and it even includes International Long Distance Calling. \r\nYou have customers waiting to talk with you right now… don’t keep them waiting. \r\nCLICK HERE https://advanceleadgeneration.com to try Talk With Web Visitor now.\r\n\r\nIf you\'d like to unsubscribe click here http://advanceleadgeneration.com/unsubscribe.aspx?d=stibuilderslimited.com\r\n', 1),
(80, 'Helmut A. Kimberly', 'projectdept@kanzalshamsprojectmgt.com', 'projectdept@kanzalshamsprojectmgt.com', 'Switzerland', 'Switzerland', 'Greetings, \r\n \r\nIt\'s a pleasure to connect with you, My name is Helmut A. Kimberly, am an investment consultant with RSL-Project Management Service C0, I have been mandated by the company to source for investment opportunities and companies seeking for funding, business loans, for its project(s). Do you have any investment or project that is seeking for capital to fund it? \r\n \r\nOur Investments financing focus is on: \r\n \r\nSeed Capital, Early-Stage, Start-Up Ventures, , Brokerage, Private Finance, Renewable Energy Project, Commercial Real Estate, Blockchain, Technology, Telecommunication, Infrastructure, Agriculture, Animal Breeding, Hospitality, Healthcare, Oil/Gas/Refinery. Application reserved for business executives and companies with proven business records in search of funding for expansion or for capital investments.. \r\n \r\nKindly contact me for further details. \r\n \r\nawait your return e.mail soonest. \r\n \r\nRegards \r\n \r\nDr. Helmut A. Kimberly \r\n \r\nMIDDLE EAST DEBT LOAN FINANCE CONSULTING \r\nAddress: 72469 Jahra Road Shuwaikh Industrial, Kuwait \r\nTel: +96550422388 \r\nEmail: rsl.fudiciary@debtloanfinanceconsultant.com', 1),
(81, 'Jimmy Swett', 'israel.swett38@yahoo.com', 'israel.swett38@yahoo.com', '', '', 'Hi there,\r\nMonthly Seo Services - Professional/ Affordable Seo Services\r\nHire the leading seo marketing company and get your website ranked on search engines. Are you looking to rank your website on search engines? Contact us now to get started -  https://digitalpromax.co/la/ Today!', 1),
(82, 'Mike Carroll\r\n', 'mikeFloobe@gmail.com', 'mikeFloobe@gmail.com', 'Netherlands Antilles', 'Netherlands Antilles', 'Hi there, \r\n \r\nMy name is Mike from Monkey Digital, \r\n \r\nAllow me to present to you a lifetime revenue opportunity of 35% \r\nThat\'s right, you can earn 35% of every order made by your affiliate for life. \r\n \r\nSimply register with us, generate your affiliate links, and incorporate them on your website, and you are done. It takes only 5 minutes to set up everything, and the payouts are sent each month. \r\n \r\nClick here to enroll with us today: \r\nhttps://www.monkeydigital.org/affiliate-dashboard/ \r\n \r\nThink about it, \r\nEvery website owner requires the use of search engine optimization (SEO) for their website. This endeavor holds significant potential for both parties involved. \r\n \r\nThanks and regards \r\nMike Carroll\r\n \r\nMonkey Digital', 1),
(83, 'Mike Ralphs\r\n', 'peterquenteeVet@gmail.com', 'peterquenteeVet@gmail.com', 'United States', 'United States', 'Howdy \r\n \r\nI have just took a look on your SEO for  stibuilderslimited.com for the ranking keywords and saw that your website could use an upgrade. \r\n \r\nWe will increase your ranks organically and safely, using only state of the art AI and whitehat methods, while providing monthly reports and outstanding support. \r\n \r\nMore info: \r\nhttps://www.digital-x-press.com/unbeatable-seo/ \r\n \r\n \r\nRegards \r\nMike Ralphs\r\nDigital X SEO Experts', 1),
(84, 'Eric Jones', 'ericjonesmyemail@gmail.com', 'ericjonesmyemail@gmail.com', '', '', 'Hi\r\n\r\nMy name’s Eric and I just found your site stibuilderslimited.com.\r\n\r\nIt’s got a lot going for it, but here’s an idea to make it even MORE effective.\r\n\r\nCLICK HERE https://advanceleadgeneration.com for a live demo now.\r\n\r\nWeb Visitors Into Leads is a software widget that’s works on your site, ready to capture any visitor’s Name, Email address and Phone Number.  It signals you the moment they let you know they’re interested – so that you can talk to that lead while they’re literally looking over your site.\r\n\r\nAnd once you’ve captured their phone number, with our new SMS Text With Lead feature, you can automatically start a text (SMS) conversation… and if they don’t take you up on your offer then, you can follow up with text messages for new offers, content links, even just “how you doing?” notes to build a relationship.\r\n\r\nCLICK HERE https://advanceleadgeneration.com to discover what Web Visitors Into Leads can do for your business.\r\n\r\nThe difference between contacting someone within 5 minutes versus a half-hour means you could be converting up to 100X more leads today!\r\n\r\nEric\r\nPS: Studies show that 70% of a site’s visitors disappear and are gone forever after just a moment. Don’t keep losing them. \r\nWeb Visitors Into Leads offers a FREE 14 days trial – and it even includes International Long Distance Calling. \r\nYou have customers waiting to talk with you right now… don’t keep them waiting. \r\nCLICK HERE https://advanceleadgeneration.com to try Talk With Web Visitor now.\r\n\r\nIf you\'d like to unsubscribe click here http://advanceleadgeneration.com/unsubscribe.aspx?d=stibuilderslimited.com\r\n', 1),
(85, 'Mike Green\r\n', 'mikedahorery@gmail.com', 'mikedahorery@gmail.com', 'Netherlands Antilles', 'Netherlands Antilles', 'Greetings \r\n \r\nThis is Mike Green\r\n \r\nLet me show you our latest research results from our constant SEO feedbacks that we have from our plans: \r\n \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nThe new Semrush Backlinks, which will make your stibuilderslimited.com SEO trend have an immediate push. \r\nThe method is actually very simple, we are building links from domains that have a high number of keywords ranking for them.  \r\n \r\nForget about the SEO metrics or any other factors that so many tools try to teach you that is good. The most valuable link is the one that comes from a website that has a healthy trend and lots of ranking keywords. \r\nWe thought about that, so we have built this plan for you \r\n \r\nCheck in detail here: \r\nhttps://www.strictlydigital.net/product/semrush-backlinks/ \r\n \r\nCheap and effective \r\n \r\nTry it anytime soon \r\n \r\n \r\nRegards \r\n \r\nMike Green\r\n \r\nmike@strictlydigital.net', 1),
(86, 'Reggielon', 'ferrazmanoel2@gmail.com', 'ferrazmanoel2@gmail.com', 'Norway', 'Norway', 'Attract 10,000 wealthy clients per day to your website stibuilderslimited.com http://elite-417871.apbet998.com/service', 1),
(87, 'Eric Jones', 'ericjonesmyemail@gmail.com', 'ericjonesmyemail@gmail.com', '', '', 'Hi stibuilderslimited.com Administrator. my name is Eric and I’m betting you’d like your website stibuilderslimited.com to generate more leads.\r\n\r\nHere’s how:\r\nWeb Visitors Into Leads is a software widget that’s works on your site, ready to capture any visitor’s Name, Email address and Phone Number.  It signals you as soon as they say they’re interested – so that you can talk to that lead while they’re still there at stibuilderslimited.com.\r\n\r\nWeb Visitors Into Leads – CLICK HERE http://advanceleadgeneration.com for a live demo now.\r\n\r\nAnd now that you’ve got their phone number, our new SMS Text With Lead feature enables you to start a text (SMS) conversation – answer questions, provide more info, and close a deal that way.\r\n\r\nIf they don’t take you up on your offer then, just follow up with text messages for new offers, content links, even just “how you doing?” notes to build a relationship.\r\n\r\nCLICK HERE http://advanceleadgeneration.com to discover what Web Visitors Into Leads can do for your business.\r\n\r\nThe difference between contacting someone within 5 minutes versus a half-hour means you could be converting up to 100X more leads today!\r\n\r\nTry Web Visitors Into Leads and get more leads now.\r\n\r\nEric\r\nPS: The studies show 7 out of 10 visitors don’t hang around – you can’t afford to lose them!\r\nWeb Visitors Into Leads offers a FREE 14 days trial – and it even includes International Long Distance Calling. \r\nYou have customers waiting to talk with you right now… don’t keep them waiting. \r\nCLICK HERE http://advanceleadgeneration.com to try Web Visitors Into Leads now.\r\n\r\nIf you\'d like to unsubscribe click here http://advanceleadgeneration.com/unsubscribe.aspx?d=stibuilderslimited.com\r\n', 1),
(88, 'Keeley Ryland', 'ryland.keeley34@gmail.com', 'ryland.keeley34@gmail.com', '', '', 'Get Google Reviews for your business reputation.\r\n\r\nIt’s very important for your business.\r\nBecause customers first time see your reviews and make a decision about your business.\r\nReviews Go a Vital role for business & it can often be the crucial tiebreaker between equidistant businesses.\r\n\r\n\r\nORDER HERE :- https://buytraffics.net/order/googlereviews.php\r\n\r\n\r\nWhy Should You Buying Google Reviews? Customer reviews from Google matter. Grow your business with Website and outrank your competitors.\r\nCustomers have more trust in other customers than in Businesses increase your business sales.\r\n\r\nWe provide :-\r\n✔ 100% Satisfaction Guaranteed\r\n✔ Manual \r\n✔ Express Delivery\r\n✔ High Quality\r\n✔ No need any admin access or password\r\n✔ 24/7 Customer Support\r\n✔ Unlimited split available\r\n\r\nORDER HERE :- https://buytraffics.net/order/googlereviews.php\r\n\r\nThanks\r\nBuy Traffics', 1),
(89, 'Sheldon Chavez', 'sheldon.chavez23@gmail.com', 'sheldon.chavez23@gmail.com', '', '', 'Hi to stibuilderslimited.com Webmaster! This is Sheldon, and for a moment, think about this…\r\n\r\n- A person does a search and lands at stibuilderslimited.com.\r\n\r\n- They stay for a minute to explore.  “I’m intrigued… but… perhaps…”\r\n\r\n- And then they hit the back button and explore the other search results instead.\r\n\r\n- Bottom line – you got an eyeball, but nothing else to prove for it.\r\n\r\n- Away they go.\r\n\r\nThis isn’t truly your fault – it happens a lot – studies show 7 out of 10 visitors to any site disappear without leaving a mark.\r\n\r\nBut you can fix that.\r\n\r\nWeb Visitors Into Leads is a widget which is operates on your site, prepared to capture any visitor’s Name, Email address, and Phone Number.  It lets you know right then and there – enabling you to call that lead as they’re really viewing your site.\r\n\r\nCLICK HERE https://advanceleadgeneration.com to test a Live Demo with Web Visitors Into Leads today to see exactly how it works.\r\n\r\nTime is money when it comes to connecting with leads – the time difference between reaching out to someone within 5 minutes against 30 minutes later can be enormous – like 100 times better!\r\n\r\nMoreover, now that you have their phone number, with our new SMS Text With Lead function, you can instantly start a text (SMS) chat… so even if you don’t secure a deal then, you can follow up with text messages for fresh offers, content links, even just “how you doing?” notes to build a relationship.\r\n\r\nEffective stuff.\r\n\r\nCLICK HERE https://advanceleadgeneration.com to find out what Web Visitors Into Leads can offer for your business.\r\n\r\nYou can be converting up to 100X more leads today!\r\n\r\nSheldon\r\nPS: Web Visitors Into Leads provides a FREE 14 days trial – and it includes International Long Distance Calls. \r\nThere are customers eager to chat with you at this moment… don’t leave them waiting. \r\nCLICK HERE https://advanceleadgeneration.com to try out Web Visitors Into Leads now.\r\n\r\nShould you prefer to unsubscribe click here http://advanceleadgeneration.com/unsubscribe.aspx?d=stibuilderslimited.com\r\n\r\nOnly a brief note - the names and email used here, Sheldon and Chavez, are placeholders and not genuine contact information. We respect transparency and wanted to make sure you’re aware! If you want to get in touch with the real person behind this message, please visit our website, and we’ll associate you with the correct individual.}\r\n', 1),
(90, 'Eric Jones', 'ericjonesmyemail@gmail.com', 'ericjonesmyemail@gmail.com', '', '', 'Dear stibuilderslimited.com Owner! this is Eric and I ran across stibuilderslimited.com a few minutes ago.\r\n\r\nLooks great… but now what?\r\n\r\nBy that I mean, when someone like me finds your website – either through Search or just bouncing around – what happens next?  Do you get a lot of leads from your site, or at least enough to make you happy?\r\n\r\nHonestly, most business websites fall a bit short when it comes to generating paying customers. Studies show that 70% of a site’s visitors disappear and are gone forever after just a moment.\r\n\r\nHere’s an idea…\r\n \r\nHow about making it really EASY for every visitor who shows up to get a personal phone call you as soon as they hit your site…\r\n \r\nYou can –\r\n  \r\nWeb Visitors Into Leads is a software widget that’s works on your site, ready to capture any visitor’s Name, Email address and Phone Number.  It signals you the moment they let you know they’re interested – so that you can talk to that lead while they’re literally looking over your site.\r\n\r\nCLICK HERE https://advanceleadgeneration.com to try out a Live Demo with Web Visitors Into Leads now to see exactly how it works.\r\n\r\nYou’ll be amazed - the difference between contacting someone within 5 minutes versus a half-hour or more later could increase your results 100-fold.\r\n\r\nIt gets even better… once you’ve captured their phone number, with our new SMS Text With Lead feature, you can automatically start a text (SMS) conversation.\r\n  \r\nThat way, even if you don’t close a deal right away, you can follow up with text messages for new offers, content links, even just “how you doing?” notes to build a relationship.\r\n\r\nPretty sweet – AND effective.\r\n\r\nCLICK HERE https://advanceleadgeneration.com to discover what Web Visitors Into Leads can do for your business.\r\n\r\nYou could be converting up to 100X more leads today!\r\n\r\nEric\r\nPS: Web Visitors Into Leads offers a FREE 14 days trial – and it even includes International Long Distance Calling. \r\nYou have customers waiting to talk with you right now… don’t keep them waiting. \r\nCLICK HERE https://advanceleadgeneration.com to try Web Visitors Into Leads now.\r\n\r\nIf you\'d like to unsubscribe click here http://advanceleadgeneration.com/unsubscribe.aspx?d=stibuilderslimited.com\r\n', 1),
(91, 'Eric Jones', 'ericjonesmyemail@gmail.com', 'ericjonesmyemail@gmail.com', '', '', 'Hi stibuilderslimited.com Owner. I just found your site, quick question…\r\n\r\nMy name’s Eric, I found stibuilderslimited.com after doing a quick search – you showed up near the top of the rankings, so whatever you’re doing for SEO, looks like it’s working well.\r\n\r\nSo here’s my question – what happens AFTER someone lands on your site?  Anything?\r\n\r\nResearch tells us at least 70% of the people who find your site, after a quick once-over, they disappear… forever.\r\n\r\nThat means that all the work and effort you put into getting them to show up, goes down the tubes.\r\n\r\nWhy would you want all that good work – and the great site you’ve built – go to waste?\r\n\r\nBecause the odds are they’ll just skip over calling or even grabbing their phone, leaving you high and dry.\r\n\r\nBut here’s a thought… what if you could make it super-simple for someone to raise their hand, say, “okay, let’s talk” without requiring them to even pull their cell phone from their pocket?\r\n  \r\nYou can – thanks to revolutionary new software that can literally make that first call happen NOW.\r\n\r\nWeb Visitors Into Leads is a software widget that sits on your site, ready and waiting to capture any visitor’s Name, Email address and Phone Number.  It lets you know IMMEDIATELY – so that you can talk to that lead while they’re still there at your site.\r\n  \r\nYou know, strike when the iron’s hot!\r\n\r\nCLICK HERE http://advanceleadgeneration.com to try out a Live Demo with Web Visitors Into Leads now to see exactly how it works.\r\n\r\nWhen targeting leads, you HAVE to act fast – the difference between contacting someone within 5 minutes versus 30 minutes later is huge – like 100 times better!\r\n\r\nThat’s why you should check out our new SMS Text With Lead feature as well… once you’ve captured the phone number of the website visitor, you can automatically kick off a text message (SMS) conversation with them. \r\n \r\nImagine how powerful this could be – even if they don’t take you up on your offer immediately, you can stay in touch with them using text messages to make new offers, provide links to great content, and build your credibility.\r\n\r\nJust this alone could be a game changer to make your website even more effective.\r\n\r\nStrike when  the iron’s hot!\r\n\r\nCLICK HERE http://advanceleadgeneration.com to learn more about everything Web Visitors Into Leads can do for your business – you’ll be amazed.\r\n\r\nThanks and keep up the great work!\r\n\r\nEric\r\nPS: Web Visitors Into Leads offers a FREE 14 days trial – you could be converting up to 100x more leads immediately!   \r\nIt even includes International Long Distance Calling. \r\nStop wasting money chasing eyeballs that don’t turn into paying customers. \r\nCLICK HERE http://advanceleadgeneration.com to try Web Visitors Into Leads now.\r\n\r\nIf you\'d like to unsubscribe click here http://advanceleadgeneration.com/unsubscribe.aspx?d=stibuilderslimited.com\r\n', 1),
(92, 'Charla Brough', 'brough.charla@outlook.com', 'brough.charla@outlook.com', '', '', 'Get Google Reviews for your business reputation.\r\n\r\nIt’s very important for your business.\r\nBecause customers first time see your reviews and make a decision about your business.\r\nReviews Go a Vital role for business & it can often be the crucial tiebreaker between equidistant businesses.\r\n\r\n\r\nORDER HERE :- https://buytraffics.net/order/googlereviews.php\r\n\r\n\r\nWhy Should You Buying Google Reviews? Customer reviews from Google matter. Grow your business with Website and outrank your competitors.\r\nCustomers have more trust in other customers than in Businesses increase your business sales.\r\n\r\nWe provide :-\r\n✔ 100% Satisfaction Guaranteed\r\n✔ Manual \r\n✔ Express Delivery\r\n✔ High Quality\r\n✔ No need any admin access or password\r\n✔ 24/7 Customer Support\r\n✔ Unlimited split available\r\n\r\nORDER HERE :- https://buytraffics.net/order/googlereviews.php\r\n\r\nThanks\r\nBuy Traffics', 1),
(93, 'Albertwhoms', 'bmaxini4.lexa@yahoo.com', 'bmaxini4.lexa@yahoo.com', 'Saudi Arabia', 'Saudi Arabia', 'URGENT! QUICK EARNINGS OF EXACTLY $1000 PER DAY IN CRYPTOCURRENCY http://the-410834.apbet998.com/bank', 1),
(94, 'Mike Chapman\r\n', 'mikedahorery@gmail.com', 'mikedahorery@gmail.com', 'New Zealand', 'New Zealand', 'If you are looking to rank your local business on Google Maps in a specific area, this service is for you. \r\n \r\nGoogle Map Stacking is a highly effective technique for ranking your GMB within a specific mile radius. \r\n \r\nMore info: \r\nhttps://www.speed-seo.net/product/google-maps-pointers/ \r\n \r\nThanks and Regards \r\nMike Chapman\r\n \r\n \r\nPS: Want a comprehensive local plan that covers everything? \r\nhttps://www.speed-seo.net/product/local-seo-bundle/', 1),
(95, 'Reggielon', 'nytmare14@yahoo.com', 'nytmare14@yahoo.com', 'Norway', 'Norway', 'Hello. \r\nIf you are the owner of the site - stibuilderslimited.com then we urgently ask you to submit an application for withdrawal of earned funds. \r\nYour personal link to log into your account - http://login-318981.pampatinyhouse.com/join', 1),
(96, 'Mike Waller\r\n', 'mikesifable@gmail.com', 'mikesifable@gmail.com', 'Taiwan', 'Taiwan', 'Hi there \r\n \r\nJust checked your stibuilderslimited.com baclink profile, I noticed a moderate percentage of toxic links pointing to your website \r\n \r\nWe will investigate each link for its toxicity and perform a professional clean up for you free of charge. \r\n \r\nStart recovering your ranks today: \r\nhttps://www.hilkom-digital.de/professional-linksprofile-clean-up-service/ \r\n \r\n \r\nRegards \r\nMike Waller\r\nHilkom Digital SEO Experts \r\nhttps://www.hilkom-digital.de/', 1),
(97, 'Eric Jones', 'ericjonesmyemail@gmail.com', 'ericjonesmyemail@gmail.com', '', '', 'Dear stibuilderslimited.com Admin. Eric here with a quick thought about your website stibuilderslimited.com...\r\n\r\nI’m on the internet a lot and I look at a lot of business websites.\r\n\r\nLike yours, many of them have great content. \r\n\r\nBut all too often, they come up short when it comes to engaging and connecting with anyone who visits.\r\n\r\nI get it – it’s hard.  Studies show 7 out of 10 people who land on a site, abandon it in moments without leaving even a trace.  You got the eyeball, but nothing else.\r\n\r\nHere’s a solution for you…\r\n\r\nWeb Visitors Into Leads is a software widget that’s works on your site, ready to capture any visitor’s Name, Email address and Phone Number.  You’ll know immediately they’re interested and you can call them directly to talk with them literally while they’re still on the web looking at your site.\r\n\r\nCLICK HERE https://advanceleadgeneration.com to try out a Live Demo with Web Visitors Into Leads now to see exactly how it works.\r\n\r\nIt could be huge for your business – and because you’ve got that phone number, with our new SMS Text With Lead feature, you can automatically start a text (SMS) conversation – immediately… and contacting someone in that 5 minute window is 100 times more powerful than reaching out 30 minutes or more later.\r\n\r\nPlus, with text messaging you can follow up later with new offers, content links, even just follow up notes to keep the conversation going.\r\n\r\nEverything I’ve just described is extremely simple to implement, cost-effective, and profitable. \r\n \r\nCLICK HERE https://advanceleadgeneration.com to discover what Web Visitors Into Leads can do for your business.\r\n\r\nYou could be converting up to 100X more eyeballs into leads today!\r\n\r\nEric\r\nPS: Web Visitors Into Leads offers a FREE 14 days trial – and it even includes International Long Distance Calling. \r\nYou have customers waiting to talk with you right now… don’t keep them waiting. \r\nCLICK HERE https://advanceleadgeneration.com to try Web Visitors Into Leads now.\r\n\r\nIf you\'d like to unsubscribe click here http://advanceleadgeneration.com/unsubscribe.aspx?d=stibuilderslimited.com\r\n\r\n', 1),
(98, 'Mike Abramson\r\n', 'mikeFloobe@gmail.com', 'mikeFloobe@gmail.com', 'Netherlands Antilles', 'Netherlands Antilles', 'Hi there, \r\n \r\nMy name is Mike from Monkey Digital, \r\n \r\nAllow me to present to you a lifetime revenue opportunity of 35% \r\nThat\'s right, you can earn 35% of every order made by your affiliate for life. \r\n \r\nSimply register with us, generate your affiliate links, and incorporate them on your website, and you are done. It takes only 5 minutes to set up everything, and the payouts are sent each month. \r\n \r\nClick here to enroll with us today: \r\nhttps://www.monkeydigital.org/affiliate-dashboard/ \r\n \r\nThink about it, \r\nEvery website owner requires the use of search engine optimization (SEO) for their website. This endeavor holds significant potential for both parties involved. \r\n \r\nThanks and regards \r\nMike Abramson\r\n \r\nMonkey Digital', 1),
(99, 'Cathern Abney', 'abney.cathern@msn.com', 'abney.cathern@msn.com', '', '', 'Greetings stibuilderslimited.com Administrator\r\n\r\nIt\'s Cathern here with a short thought about your website stibuilderslimited.com...\r\n\r\nI’m throughout the internet quite a bit and I examine a lot of business websites.\r\n\r\nJust like yours, a number of them have great content.\r\n\r\nBut all too often, they come up short when it comes to engaging and bonding with anybody who visits.\r\n\r\nI understand – it’s hard. Studies show 7 out of 10 people who land on a site, abandon it in moments without leaving a trace. You got the eyeball, but nothing else.\r\n\r\nI have a solution for you…\r\n\r\nLead Capture is a software widget that’s works on your site, set to capture any visitor’s Name, Email address, and Phone Number. You’ll know right away they’re interested and you can call them directly to speak with them literally while they’re still on the web looking at your site.\r\n\r\nCLICK HERE http://jumboleadmagnet.com to try out a Live Demo with Lead Capture now to see specifically how it works.\r\n\r\nIt could be huge for your business – and because you’ve got that phone number, with our new SMS Text With Lead feature, you can automatically start a text (SMS) conversation – immediately… and contacting someone in that 5-minute window is 100 times more powerful than reaching out 30 minutes or more later.\r\n\r\nMoreover, with text messaging you can follow up later with new offers, content links, even just follow-up notes to maintain the conversation going.\r\n\r\nAll I’ve just described is very simple to implement, cost-effective, and profitable.\r\n\r\nCLICK HERE http://jumboleadmagnet.com to find out what Instant Engagement Tool can do for your business.\r\n\r\nYou might be converting up to 100X more eyeballs into leads today!\r\n\r\nCathern\r\nPS: Lead Capture offers a FREE 14 days trial – and it even includes International Long Distance Calling.\r\nYou have customers eager to talk with you immediately… don’t keep them waiting.\r\nCLICK HERE http://jumboleadmagnet.com to test Instant Engagement Tool now.\r\n\r\nIf you\'d prefer to unsubscribe click here http://jumboleadmagnet.com/unsubscribe.aspx?d=stibuilderslimited.com\r\n\r\nSimply a quick note - the names and email address utilized in this note, Cathern and Abney, are stand-ins and not real contact information. We esteem transparency and aimed to ensure you are aware of this! In case you aspire to make contact with the true one responsible for this communication, kindly check out our site, and we’ll link you with the right entity.\r\n', 1),
(100, 'ScottDus', 'smeier@habegger.ch', 'smeier@habegger.ch', 'Spain', 'Spain', 'KI + KRYPTOWAHRUNG = PASSIVES EINKOMMEN AB 1000 EURO PRO TAG http://euro-617532.gurujitourandtravels.com/app', 1),
(101, 'Jim Stewart', 'brittany.stewart@gmail.com', 'brittany.stewart@gmail.com', '', '', 'Hi there,\r\nMonthly Seo Services - Professional/ Affordable Seo Services\r\nHire the leading seo marketing company and get your website ranked on search engines. Are you looking to rank your website on search engines? Contact us now to get started - https://digitalpromax.co/la/  Today!\r\n\r\nPsst.. we will also do web design and build complete website. Wordpress and Ecommerce sites development. Click here: https://wpexpertspro.co/website/', 1);
INSERT INTO `realstateapp_contactmessage` (`id`, `name`, `email`, `property_plot_type`, `location`, `apartment_size`, `message`, `status`) VALUES
(102, 'Eric Jones', 'ericjonesmyemail@gmail.com', 'ericjonesmyemail@gmail.com', '', '', 'To the stibuilderslimited.com Admin. I just found your site, quick question…\r\n\r\nMy name’s Eric, I found stibuilderslimited.com after doing a quick search – you showed up near the top of the rankings, so whatever you’re doing for SEO, looks like it’s working well.\r\n\r\nSo here’s my question – what happens AFTER someone lands on your site?  Anything?\r\n\r\nResearch tells us at least 70% of the people who find your site, after a quick once-over, they disappear… forever.\r\n\r\nThat means that all the work and effort you put into getting them to show up, goes down the tubes.\r\n\r\nWhy would you want all that good work – and the great site you’ve built – go to waste?\r\n\r\nBecause the odds are they’ll just skip over calling or even grabbing their phone, leaving you high and dry.\r\n\r\nBut here’s a thought… what if you could make it super-simple for someone to raise their hand, say, “okay, let’s talk” without requiring them to even pull their cell phone from their pocket?\r\n  \r\nYou can – thanks to revolutionary new software that can literally make that first call happen NOW.\r\n\r\nWeb Visitors Into Leads is a software widget that sits on your site, ready and waiting to capture any visitor’s Name, Email address and Phone Number.  It lets you know IMMEDIATELY – so that you can talk to that lead while they’re still there at your site.\r\n  \r\nYou know, strike when the iron’s hot!\r\n\r\nCLICK HERE http://advanceleadgeneration.com to try out a Live Demo with Web Visitors Into Leads now to see exactly how it works.\r\n\r\nWhen targeting leads, you HAVE to act fast – the difference between contacting someone within 5 minutes versus 30 minutes later is huge – like 100 times better!\r\n\r\nThat’s why you should check out our new SMS Text With Lead feature as well… once you’ve captured the phone number of the website visitor, you can automatically kick off a text message (SMS) conversation with them. \r\n \r\nImagine how powerful this could be – even if they don’t take you up on your offer immediately, you can stay in touch with them using text messages to make new offers, provide links to great content, and build your credibility.\r\n\r\nJust this alone could be a game changer to make your website even more effective.\r\n\r\nStrike when  the iron’s hot!\r\n\r\nCLICK HERE http://advanceleadgeneration.com to learn more about everything Web Visitors Into Leads can do for your business – you’ll be amazed.\r\n\r\nThanks and keep up the great work!\r\n\r\nEric\r\nPS: Web Visitors Into Leads offers a FREE 14 days trial – you could be converting up to 100x more leads immediately!   \r\nIt even includes International Long Distance Calling. \r\nStop wasting money chasing eyeballs that don’t turn into paying customers. \r\nCLICK HERE http://advanceleadgeneration.com to try Web Visitors Into Leads now.\r\n\r\nIf you\'d like to unsubscribe click here http://advanceleadgeneration.com/unsubscribe.aspx?d=stibuilderslimited.com\r\n', 1),
(103, 'PedroHak', 'cedric.nicolas@urbanet.ch', 'cedric.nicolas@urbanet.ch', 'Austria', 'Austria', 'Investieren Sie klug und ernten Sie taglich 1000 EUR! http://euros-615882.mariuspopescu.com/ai', 1),
(104, 'Ernestina Marcum', 'marcum.ernestina37@gmail.com', 'marcum.ernestina37@gmail.com', '', '', 'Get Google Reviews for your business reputation.\r\n\r\nIt’s very important for your business.\r\nBecause customers first time see your reviews and make a decision about your business.\r\nReviews Go a Vital role for business & it can often be the crucial tiebreaker between equidistant businesses.\r\n\r\n\r\nORDER HERE :- https://buytraffics.net/order/googlereviews.php\r\n\r\n\r\nWhy Should You Buying Google Reviews? Customer reviews from Google matter. Grow your business with Website and outrank your competitors.\r\nCustomers have more trust in other customers than in Businesses increase your business sales.\r\n\r\nWe provide :-\r\n✔ 100% Satisfaction Guaranteed\r\n✔ Manual \r\n✔ Express Delivery\r\n✔ High Quality\r\n✔ No need any admin access or password\r\n✔ 24/7 Customer Support\r\n✔ Unlimited split available\r\n\r\nORDER HERE :- https://buytraffics.net/order/googlereviews.php\r\n\r\nThanks\r\nBuy Traffics', 1),
(105, 'Jones Eloff', 'eloffjones@gmail.com', 'eloffjones@gmail.com', 'Belgium', 'Belgium', 'PRIVATE TRANSACTION \r\n \r\nI propose a partnership to manage over invoice petroleum oil and gas strategic reserve resources. Please response for fund credentials and detailed information to: joneseloff.mr@hotmail.com \r\n \r\nWe look forward to the opportunity to work together and create a mutual beneficial partnership. \r\n \r\nThank you \r\n \r\nRegards \r\n \r\nJones Eloff', 1),
(106, 'Bernadette O\'Malley', 'omalley.bernadette@hotmail.com', 'omalley.bernadette@hotmail.com', '', '', 'Hello stibuilderslimited.com Manager!\r\n\r\nMy name’s Bernadette and I just ran across your site at stibuilderslimited.com...\r\n\r\nI located it after a swift search, so your SEO’s working out…\r\n\r\nMaterial looks decent…\r\n\r\nOne thing’s missing though…\r\n\r\nA RAPID, CONVENIENT way to communicate with you NOW.\r\n\r\nBecause research show that a visitor like me will only hang out a few seconds – 7 out of 10 disappear almost instantly, Browse Browse Browse… then gone.\r\n\r\nI have the answer:\r\n\r\nWeb Visitors Into Leads is a software widget that’s operates on your website, set to capture any user’s Name, Email address, and Phone Number. You will know instantly they’re intrigued and you can call them directly to SPEAK with them - literally while they’re still on the web looking at your website.\r\n\r\nCLICK HERE https://bit.ly/3LPltcD to test a Live Demo with Lead Conversion Tool now to see just how it works and even give it a try… it could be huge for your business.\r\n\r\nPlus, now that you’ve got that phone number, with our new SMS Text With Lead feature, you can automatically start a text (SMS) conversation immediately… which is so powerful, because linking up with someone within the first 5 minutes is 100 times more effective than waiting 30 minutes or more later.\r\n\r\nThe new text messaging feature lets you follow up regularly with new offers, content links, even just follow-up notes to develop a relationship.\r\n\r\nAll I’ve just described is incredibly simple to implement, cost-effective, and lucrative.\r\n\r\nCLICK HERE https://bit.ly/3LPltcD to discover what Lead Conversion Tool can do for your company, maybe converting up to 100X more viewers into leads right now!\r\n\r\nBernadette\r\nPS: Web Visitors Into Leads offers a FREE 14 days trial – and it even includes International Long Distance Calling.\r\nYou have prospects waiting to speak with you at this moment… don’t keep them waiting.\r\nCLICK HERE https://bit.ly/3LPltcD to try Lead Conversion Tool now.\r\n\r\nIf you\'d prefer to unsubscribe click here https://bit.ly/3rD0G5c\r\n\r\nOnly a rapid notification - the identities and email employed here, Bernadette and O\'Malley, are substitutes and not genuine information. We cherish candor and wished to ensure you’re informed! Should you want to communicate with the genuine individual behind this communication, please check out our site, and we’ll connect you with the right individual.\r\n', 1),
(107, 'WilliamMon', 'reymendez78@gmail.com', 'reymendez78@gmail.com', 'Bulgaria', 'Bulgaria', 'Get on the Fast Track to Wealth - $1000 Per Day Guaranteed http://method-817834.svvclinic.com/sell', 1),
(108, 'PhilDal', 'alvinbbm41@gmail.com', 'alvinbbm41@gmail.com', 'Georgia', 'Germany', 'Salam, qiymətinizi bilmək istədim.', 1),
(109, 'Mike MacDonald\r\n', 'mikesifable@gmail.com', 'mikesifable@gmail.com', 'United States', 'United States', 'Hi there, \r\n \r\nI have reviewed your domain in MOZ and have observed that you may benefit from an increase in authority. \r\n \r\nOur solution guarantees you a high-quality domain authority score within a period of three months. This will increase your organic visibility and strengthen your website authority, thus making it stronger against Google updates. \r\n \r\nCheck out our deals for more details. \r\nhttps://www.monkeydigital.co/domain-authority-plan/ \r\n \r\nNEW: Ahrefs Domain Rating \r\nhttps://www.monkeydigital.co/ahrefs-seo/ \r\n \r\nThanks and regards \r\nMike MacDonald\r\n', 1),
(110, 'Roseann Chin', 'chin.roseann@gmail.com', 'chin.roseann@gmail.com', '', '', 'Salutations stibuilderslimited.com Administrator\r\n\r\nMy name’s Roseann and I recently discovered your webpage - stibuilderslimited.com - in the search listings.\r\n\r\nHere’s what that implies to me…\r\n\r\nYour SEO’s functioning.\r\n\r\nYou’re receiving eyeballs – at least mine.\r\n\r\nYour content’s pretty good, wouldn’t change a single thing.\r\n\r\nBUT…\r\n\r\nEyeballs don’t pay the invoices.\r\n\r\nCUSTOMERS do.\r\n\r\nAnd research indicate that 7 out of 10 visitors to a site like stibuilderslimited.com will stop by, have a look, and then head for the hills without doing anything else.\r\n\r\nIt’s like they never even were even there there.\r\n\r\nYou can rectify this.\r\n\r\nYou can make it it super-simple for them to show interest, say, “okay, let’s talk” without requiring them to even pull their phone from their pocket… courtesy of Web Visitors Into Leads.\r\n\r\nVisitor to Lead Widget is a tool that lives on your site, prepared and waiting to capture to grab any user’s Name, Email address, and Phone Number. It allows you know immediately immediately – so you can speak with that lead right away… BEFORE they head for those hills.\r\n\r\nCLICK HERE https://bit.ly/3LPltcD to experience a Live Demo with Web Visitors Into Leads right now to see exactly precisely how it operates.\r\n\r\nNow it’s also true it’s also true that when reaching out to hot leads, you MUST act fast fast – the difference between contacting someone someone within 5 minutes 5 minutes versus 30 minutes later is huge – like 100 times better!\r\n\r\nThat’s what makes our new SMS Text With Lead feature so potent… you’ve got their phone number, so now you can you can start a text message a text message (SMS) conversation with them with them… so even if they don’t take you up take you up on your offer immediately, you continue to text them to text them them new offers, new content, and new reasons to do business with you.\r\n\r\nThis could change everything change everything for you and your company.\r\n\r\nCLICK HERE https://bit.ly/3LPltcD to find out about everything Web Visitors Into Leads can do Lead Conversion Software can do and start turing eyeballs into cash.\r\n\r\nRoseann\r\nPS: Web Visitors Into Leads offers a FREE 14 days trial!\r\nIt even includes includes International Long Distance Calling.\r\nPaying customers are out there waiting.\r\nStarting connecting today by CLICKING HERE https://bit.ly/3LPltcD to try Web Visitors Into Leads Lead Conversion Software now.\r\n\r\nIf you\'d like to unsubscribe click here https://bit.ly/3rD0G5c\r\n\r\nMerely a quick note - the identities and email address utilized in this message, Roseann and Chin, are stand-ins and not really actual contact information. We appreciate honesty and wanted to confirm you are aware of this! In case you aspire to get in touch with the actual person behind this note, kindly check out our website, and we’ll connect you with the appropriate entity.\r\n', 1),
(111, 'Mike Audley\r\n', 'peterquenteeVet@gmail.com', 'peterquenteeVet@gmail.com', 'United States', 'United States', 'Hi \r\n \r\nI have just took an in depth look on your  stibuilderslimited.com for the ranking keywords and saw that your website could use an upgrade. \r\n \r\nWe will enhance your ranks organically and safely, using only state of the art AI and whitehat methods, while providing monthly reports and outstanding support. \r\n \r\nMore info: \r\nhttps://www.digital-x-press.com/unbeatable-seo/ \r\n \r\n \r\nRegards \r\nMike Audley\r\nDigital X SEO Experts', 1),
(112, 'Megan Bury', 'megan.bury@gmail.com', 'megan.bury@gmail.com', '', '', 'To the stibuilderslimited.com Administrator!\r\n\r\nI\'m Megan and I just ran across your site at stibuilderslimited.com...\r\n\r\nI located it after a swift search, so your SEO’s working out…\r\n\r\nMaterial looks decent…\r\n\r\nOne thing’s missing though…\r\n\r\nA FAST, SIMPLE way to get in touch with you NOW.\r\n\r\nBecause data show that a web lead like me will only linger a few seconds – 7 out of 10 leave almost immediately, Browse Browse Click… then gone.\r\n\r\nI have the solution:\r\n\r\nVisitor Engagement Widget is a software that’s works on your site, set to capture any user’s Name, Email address, and Phone Number. You’ll know right away they’re interested and you can call them immediately to CHAT with them - really while they’re still on the internet looking at your site.\r\n\r\nCLICK HERE https://bit.ly/3LPltcD to experience a Live Demo with Lead Conversion Tool now to see exactly how it works and even give it a try… it could be huge for your enterprise.\r\n\r\nPlus, now that you’ve got that phone number, with our new SMS Text With Lead feature, you can instantly start a text (SMS) conversation immediately… which is so powerful, because getting in touch with someone within the first 5 minutes is 100 times more efficient than waiting 30 minutes or more later.\r\n\r\nThe new text messaging feature lets you keep in touch frequently with new offers, content links, even just follow-up notes to build a relationship.\r\n\r\nEverything I’ve just described is very simple to implement, cost-effective, and lucrative.\r\n\r\nCLICK HERE https://bit.ly/3LPltcD to learn what Visitor Engagement Widget can do for your company, potentially converting up to 100X more viewers into leads now!\r\n\r\nMegan\r\nPS: Web Visitors Into Leads offers a FREE 14 days trial – and it even includes International Long Distance Calling.\r\nYou have customers waiting to speak with you at this moment… don’t keep them waiting.\r\nCLICK HERE https://bit.ly/3LPltcD to use Visitor Engagement Widget now.\r\n\r\nIf you\'d like to unsubscribe click here https://bit.ly/3rD0G5c\r\n\r\nOnly a brief note - the names and email used here, Megan and Bury, are placeholders and not really actual information. We cherish transparency and wanted to make sure you are informed! In case you want to connect with the true entity behind this message, please go to our website, and we’ll unite you with the proper entity.\r\n', 1),
(113, 'Michaela Murry', 'michaela.murry@gmail.com', 'michaela.murry@gmail.com', '', '', 'To the stibuilderslimited.com Admin. it\'s Eric and I found stibuilderslimited.com some moments ago.\r\n\r\nAppears great… but now what?\r\n\r\nBy that I mean, once someone such as myself finds your website –  via searching or just bouncing around – what happens next? Are you getting a lot of leads from your site, or at least enough to make you happy?\r\n\r\nTo be honest, most business websites come a bit short in terms of it comes to creating paying customers. Data show that 70% of a site’s visitors disappear and are gone forever after just a moment.\r\n\r\nHere is an idea…\r\n\r\nHow about making it really EASY for each visitor who arrives to get a personal phone call from you as soon as they hit your site…\r\n\r\nThis is possible –\r\n\r\nWeb Visitors Into Leads is a tool widget that’s operates on your site, set to capture every visitor’s Name, Email address and Phone Number. It signals you the moment they let you know they’re interested – so that you can speak to that lead while they’re literally browsing your site.\r\n\r\nCLICK HERE https://bit.ly/LeadGena to check out a Live Demo with Web Visitors Into Leads now to understand exactly how it works.\r\n\r\nYou will be surprised - the difference between connecting with someone within just 5 minutes versus a half-hour or more later could boost your results 100-fold.\r\n\r\nIt gets even better… after you’ve grabbed their phone number, with our new SMS Text With Lead capability, you can instantly start a text (SMS) chat.\r\n\r\nThus, even if you don’t seal a deal instantly, you can follow up with text messages for fresh deals, content links, even just “how you doing?” notes to build a relationship.\r\n\r\nPretty sweet – AND effective.\r\n\r\nCLICK HERE https://bit.ly/LeadGena to learn what Web Visitors Into Leads can do for your business.\r\n\r\nYou can be converting up to 100X more leads as we speak!\r\n\r\nEric\r\nPS: Web Visitors Into Leads offers a FREE 14 days trial – and it also includes International Long Distance Calling. \r\nYou have customers waiting to chat with you right now… don’t leave them waiting. \r\nCLICK HERE https://bit.ly/LeadGena to try Web Visitors Into Leads now.\r\n\r\nIf you\'d prefer to unsubscribe click here https://bit.ly/3rD0G5c\r\n\r\nOnly a brief note - the names and email used in this email, Michaela and Murry, are dummy data and not genuine contact details. We respect transparency and wanted to make  you’re aware! If you wish to get in touch with the real person responsible for this message, kindly visit our website, and we’ll associate you with the correct individual.}\r\n', 1),
(114, 'Erica Johnston', 'johnston.erica@gmail.com', 'johnston.erica@gmail.com', '', '', 'stibuilderslimited.com Owner, Greetings! I just found your website, brief inquiry…\r\n\r\nMy name’s Erica, I discovered stibuilderslimited.com after conducting a rapid search – you appeared up close to the peak of the search rankings, so whatsoever you’re doing for SEO, appears like it’s operating well.\r\n\r\nSo here’s my question – what exactly transpires AFTER an individual arrives on your website? Anything at all?\r\n\r\nResearch informs us at least 70% of the individuals who find your site, after a swift glance, they disappear… forever.\r\n\r\nThis means that all of the the work and attempt you put in into getting them to arrive, goes down the tubes.\r\n\r\nWhy on earth would you wish all great work and effort – and the great website you’ve built – go to waste?\r\n\r\nAs the probabilities are they’ll just skip over calling or even grabbing their cell phone, leaving you in the lurch.\r\n\r\nBut however, here’s a thought for you… what you could make it extremely simple for someone raise their hand, “okay, let’s talk” without needing them to even pull out their phone from their pocket to revolutionary new software can literally make that first ever call NOW.\r\n\r\nWeb Visitors Into Leads is a software widget that sits on your site and waiting to capture any visitor’s Name, Email address and Phone Number. It lets you know IMMEDIATELY – so that you can talk to that lead they’re still there at your site, you know, strike the iron’s hot!\r\n\r\nCLICK HERE https://bit.ly/LeadGena to try a Live Demo with Web Visitors Into Leads now see exactly how it works targeting leads, you HAVE to act – the difference between contacting someone within minutes 30 minutes later is huge 100 times better!\r\n\r\nThat’s you should check out our new SMS Text With Lead feature as well… once you’ve captured phone of the website visitor, you can automatically off a text message (SMS) conversation with them.\r\n\r\nImagine how powerful could be – even if they don’t take you up on your offer, you can stay touch with them using text messages to make new offers, provide links to great, and build your credibility, just this alone could be a game changer to make website even more effective when the iron’s!\r\n\r\nCLICK HERE https://bit.ly/LeadGena to learn more about everything Visitors Into Leads can do for your business – you’ll be amazed and keep the great!\r\n\r\nErica\r\nPS: Web Visitors Into Leads offers a FREE 14 days trial – you could be converting up to 100x more leads! It even includes International Long Distance Calling wasting chasing that don’t into paying. CLICK HERE https://bit.ly/LeadGena to try Web Visitors Into Leads now you\'d like unsubscribe here https://bit.ly/3rD0G5c\r\n\r\nJust a quick note - the names and email used here, are placeholders and not real contact information. We value transparency and wanted to make sure you’re aware! If you wish to get touch the real person behind message, please visit our website we’ll connect with the right.}\r\n', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_eventgallery`
--

CREATE TABLE `realstateapp_eventgallery` (
  `id` bigint NOT NULL,
  `picture` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_eventgallery`
--

INSERT INTO `realstateapp_eventgallery` (`id`, `picture`, `status`) VALUES
(1, 'event_gallery/nsb.webp', 1),
(2, 'event_gallery/nsb-2.jpg', 1),
(3, 'event_gallery/nsb-3.jpg', 1),
(4, 'event_gallery/interior-1.jpg', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_faq`
--

CREATE TABLE `realstateapp_faq` (
  `id` bigint NOT NULL,
  `question` varchar(800) NOT NULL,
  `answer` longtext NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_faq`
--

INSERT INTO `realstateapp_faq` (`id`, `question`, `answer`, `status`) VALUES
(1, 'Can I search for a rental property?', 'Yes, you can search and choose a property for rental purpose as per availability.', 1),
(2, 'What kinds of properties are listed for sale?', ' Condominiums, apartments, houses, villas, raw land plots, commercial space and many others.', 1),
(3, 'How do I find a property?', ' Arisha Group.com Portal is designed to make this as easy as possible. Select Search for property listings, click go, and then narrow your search based on country, area, property type, size, and other criteria. Once you\'ve found a property you are interested in, select contact seller and we\'ll email them with your inquiry and for you may add the property/ies on “My Favorites” which is an exclusive feature of bdhousing.com; which will help you to find out your exact choice and we hope it will help you to save your valuable time. The seller can then contact you directly.', 1),
(4, 'What is the stibuilderslimited.com Portal?', ' The “ stibuilderslimited.com” is an online community for real estate professionals run on behalf of its members. Our goal is to create a valuable resource of information and ideas for real estate professionals and their clients. We aim to help empower people by providing tools to help promote business and connect with peers all over the country and also in abroad.', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_hotnumber`
--

CREATE TABLE `realstateapp_hotnumber` (
  `id` bigint NOT NULL,
  `title` varchar(500) NOT NULL,
  `number` varchar(15) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_hotnumber`
--

INSERT INTO `realstateapp_hotnumber` (`id`, `title`, `number`, `status`) VALUES
(1, 'Buy Property', '01322301173', 1),
(2, 'Land Owners', '01923505050', 1),
(3, 'Customer Care', '01322301173', 1),
(4, 'Interior Design', '01923505050', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_privacypolicy`
--

CREATE TABLE `realstateapp_privacypolicy` (
  `id` bigint NOT NULL,
  `title` varchar(500) NOT NULL,
  `picture` varchar(100) NOT NULL,
  `privacy_policy` longtext NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_privacypolicy`
--

INSERT INTO `realstateapp_privacypolicy` (`id`, `title`, `picture`, `privacy_policy`, `status`) VALUES
(1, 'title', 'images/testimonial_image/pp.jpg', '<h3 style=\"text-align:justify\"><strong><span style=\"color:#1abc9c\">Privacy &amp; Policy</span></strong></h3>\r\n\r\n<p style=\"text-align:justify\">This Privacy Policy governs how the STI Builders collects, uses, maintains, and discloses information collected from users (each, a &quot;User&quot;) of the https://www.stibuilderslimited.com/ website (&quot;Site&quot;).</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Personal identification information</strong></h3>\r\n\r\n<p style=\"text-align:justify\">We may collect personal identification information from Users in a variety of ways, including, but not limited to, when Users visit our site, register on the site, place an order, fill out a form, and in connection with other activities, services, features or resources we make available on our Site. Users may be asked for, as appropriate, a name, email address, and phone number. Users may, however, visit our Site anonymously. We will collect personal identification information from Users only if they voluntarily submit such information to us. Users can always refuse to supply personal identification information, except that it may prevent them from engaging in certain Site related activities.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Non-personal identification information</strong></h3>\r\n\r\n<p style=\"text-align:justify\">We may collect non-personal identification information about Users whenever they interact with our Site. Non-personal identification information may include the browser name, the type of computer, and technical information about Users means of connection to our Sites, such as the operating system and the Internet service providers utilized and other similar information.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Web browser cookies</strong></h3>\r\n\r\n<p style=\"text-align:justify\">Our Site may use &quot;cookies&quot; to enhance the User experience. Users&#39; web browser places cookies on their hard drive for record-keeping purposes and sometimes to track information about them. Users may choose to set their web browser to refuse cookies or to alert you when cookies are being sent. If they do so, note that some parts of the Site may not function properly.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>How we use collected information</strong></h3>\r\n\r\n<p style=\"text-align:justify\">STI Builders may collect and use Users&#39; personal information for the following purposes:</p>\r\n\r\n<ul>\r\n	<li style=\"text-align:justify\"><em>To run and operate our Site</em><br />\r\n	We may need your information to display content on the Site correctly.</li>\r\n	<li style=\"text-align:justify\"><em>To improve customer service</em><br />\r\n	The information you provide helps us respond to your customer service requests and support needs more efficiently.</li>\r\n	<li style=\"text-align:justify\"><em>To personalize user experience</em><br />\r\n	We may use information in the aggregate to understand how our Users as a group use the services and resources provided on our Site.</li>\r\n	<li style=\"text-align:justify\"><em>To improve our Site</em><br />\r\n	We may use the feedback you provide to improve our products and services.</li>\r\n	<li style=\"text-align:justify\"><em>To send periodic emails</em><br />\r\n	We may use the email address to send User information and updates about their order. It may also be used to respond to their inquiries, questions, and/or other requests.</li>\r\n</ul>\r\n\r\n<h3 style=\"text-align:justify\"><strong>How we protect your information</strong></h3>\r\n\r\n<p style=\"text-align:justify\">We adopt appropriate data collection, storage, and processing practices and security measures to protect against unauthorized access, alteration, disclosure, or destruction of your personal information, username, password, transaction information, and data stored on our Site.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Sharing your personal information</strong></h3>\r\n\r\n<p style=\"text-align:justify\">We do not sell, trade, or rent Users&#39; personal identification information to others. We may share generic aggregated demographic information not linked to any personal identification information regarding visitors and users with our business partners, trusted affiliates, and advertisers for the purposes outlined above. We may use third-party service providers to help us operate our business and the Site or administer activities on our behalf, such as sending out newsletters or surveys. We may share your information with these third parties for those limited purposes provided that you have given us your permission.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Electronic newsletters</strong></h3>\r\n\r\n<p style=\"text-align:justify\">If User decides to opt-in to our mailing list, they will receive emails that may include company news, updates, related product or service information, etc. We may use third-party service providers to help us operate our business and the Site or administer activities on our behalf, such as sending out newsletters or surveys. We may share your information with these third parties for those limited purposes provided that you have given us your permission.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Advertising</strong></h3>\r\n\r\n<p style=\"text-align:justify\">Ads appearing on our site may be delivered to Users by advertising partners, who may set cookies. These cookies allow the ad server to recognize your computer each time they send you an online advertisement to compile non-personal identification information about you or others who use your computer. This information allows ad networks to, among other things, deliver targeted advertisements that they believe will be of most interest to you. This privacy policy does not cover the use of cookies by any advertisers.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Google Adsense</strong></h3>\r\n\r\n<p style=\"text-align:justify\">Some of the ads may be served by Google. Google&#39;s use of the DART cookie enables it to serve ads to Users based on their visit to our Site and other sites on the Internet. DART uses &quot;non-personally identifiable information&quot; and does NOT track personal information about you, such as your name, email address, physical address, etc. You may opt-out of the use of the DART cookie by visiting the Google ad and content network privacy policy at&nbsp;<a href=\"https://www.google.com/privacy_ads.html\">https://www.google.com/privacy_ads.html</a></p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Changes to this privacy policy</strong></h3>\r\n\r\n<p style=\"text-align:justify\">STI Builders&nbsp;has the discretion to update this privacy policy at any time. When we do, we will post a notification on the main page of our Site and send you an email. We encourage Users to frequently check this page for any changes to stay informed about how we are helping to protect the personal information we collect. You acknowledge and agree that it is your responsibility to review this privacy policy periodically and become aware of modifications.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Your acceptance of these terms</strong></h3>\r\n\r\n<p style=\"text-align:justify\">By using this Site, you signify your acceptance of this policy. If you do not agree to this policy, please do not use our Site. Your continued use of the Site following the posting of changes to this policy will be deemed your acceptance of those changes.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Contacting us</strong></h3>\r\n\r\n<p style=\"text-align:justify\">If you have any questions about this Privacy Policy, the practices of this site, or your dealings with this site, please contact us.</p>\r\n\r\n<p style=\"text-align:justify\">This document was last updated on September 7, 2022</p>', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_qualityadd`
--

CREATE TABLE `realstateapp_qualityadd` (
  `id` bigint NOT NULL,
  `quality_title` varchar(500) NOT NULL,
  `quality_text` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_qualityadd`
--

INSERT INTO `realstateapp_qualityadd` (`id`, `quality_title`, `quality_text`, `image`, `status`) VALUES
(1, 'We Never Compromise With Quality and Best Practices', 'We have set our own standards that always keeps us on the right track so we can build the real Home for Peace for you and your family. We never compromise with the quality at any stage of a building project. From project site selection to modern fittings, we maintain the best practices prevailing in the industry. The quality of our homes has already got valuable recognition from our clients and the professionals in the industry. Our quality has lead to making a successful real estate brand in Bangladesh in a short period of time.', 'quality_image/about.jpg', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_servicedetails`
--

CREATE TABLE `realstateapp_servicedetails` (
  `id` bigint NOT NULL,
  `service_banner` varchar(100) NOT NULL,
  `service_title` varchar(300) NOT NULL,
  `service_image` varchar(100) NOT NULL,
  `service_description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `service_name_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_servicedetails`
--

INSERT INTO `realstateapp_servicedetails` (`id`, `service_banner`, `service_title`, `service_image`, `service_description`, `status`, `service_name_id`) VALUES
(1, '', '', '', '', 1, 1),
(2, '', '', '', '', 1, 2),
(3, '', '', '', '', 1, 3),
(4, '', '', '', '', 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_serviceentry`
--

CREATE TABLE `realstateapp_serviceentry` (
  `id` bigint NOT NULL,
  `service_name` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_serviceentry`
--

INSERT INTO `realstateapp_serviceentry` (`id`, `service_name`, `status`) VALUES
(1, 'Construction', 1),
(2, 'Resale Flat', 1),
(3, 'Land Sharing & Flat Position', 1),
(4, 'Housing', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_sisternconcerndetails`
--

CREATE TABLE `realstateapp_sisternconcerndetails` (
  `id` bigint NOT NULL,
  `sister_concern_banner` varchar(100) NOT NULL,
  `sister_concern_image` varchar(100) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `mobile` varchar(14) NOT NULL,
  `email` varchar(254) NOT NULL,
  `facebook_link` varchar(1200) NOT NULL,
  `twitter_link` varchar(1200) NOT NULL,
  `linkedin_link` varchar(1200) NOT NULL,
  `youtube_link` varchar(1200) NOT NULL,
  `service_description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `sister_concern_name_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_sisternconcerndetails`
--

INSERT INTO `realstateapp_sisternconcerndetails` (`id`, `sister_concern_banner`, `sister_concern_image`, `address`, `mobile`, `email`, `facebook_link`, `twitter_link`, `linkedin_link`, `youtube_link`, `service_description`, `status`, `sister_concern_name_id`) VALUES
(1, '', '', '', '', '', '', '', '', '', '', 1, 1),
(2, '', '', '', '', '', '', '', '', '', '', 1, 2),
(3, '', '', '', '', '', '', '', '', '', '', 1, 3),
(4, '', '', '', '', '', '', '', '', '', '', 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_sisternconcernentry`
--

CREATE TABLE `realstateapp_sisternconcernentry` (
  `id` bigint NOT NULL,
  `sister_concern_name` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_sisternconcernentry`
--

INSERT INTO `realstateapp_sisternconcernentry` (`id`, `sister_concern_name`, `status`) VALUES
(1, 'STI Firms', 1),
(2, 'Noor Jahan Charitable Society', 1),
(3, 'SI Green Palli & Firms Ltd', 1),
(4, 'N.Q Collection Ltd', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_sliderbanner`
--

CREATE TABLE `realstateapp_sliderbanner` (
  `id` bigint NOT NULL,
  `title` longtext NOT NULL,
  `slider_banner` varchar(100) NOT NULL,
  `short_description` longtext NOT NULL,
  `slider_order` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `button_text` varchar(100) NOT NULL,
  `button_url` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_sliderbanner`
--

INSERT INTO `realstateapp_sliderbanner` (`id`, `title`, `slider_banner`, `short_description`, `slider_order`, `status`, `button_text`, `button_url`) VALUES
(14, 'STI South palace', 'slider_banner/South Palace.webp', '', 3, 1, '', ''),
(16, 'STI Lake drive paradise', 'slider_banner/lake-drive-paradise.webp', '', 1, 1, '', ''),
(22, 'STI ORCHID', 'slider_banner/WhatsApp Image 2023-03-01 at 11.00.04 AM (1).jpeg', '', 4, 1, '', ''),
(23, 'STI RORAL TOWER', 'slider_banner/WhatsApp Image 2023-03-01 at 11.00.04 AM.jpeg', '', 2, 1, '', '');

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_teammemberinfo`
--

CREATE TABLE `realstateapp_teammemberinfo` (
  `id` bigint NOT NULL,
  `member_name` varchar(200) NOT NULL,
  `member_image` varchar(100) NOT NULL,
  `member_disignation` varchar(300) NOT NULL,
  `facebook_link` varchar(200) NOT NULL,
  `twitter_link` varchar(200) NOT NULL,
  `instragram_link` varchar(200) NOT NULL,
  `member_order` int NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_teammemberinfo`
--

INSERT INTO `realstateapp_teammemberinfo` (`id`, `member_name`, `member_image`, `member_disignation`, `facebook_link`, `twitter_link`, `instragram_link`, `member_order`, `status`) VALUES
(1, 'Full Name', '', 'Chairman', '', '', '', 1, 1),
(2, 'Md. Eshaq Ali', 'images/Team_member/md.jpeg', 'Managing Director', '', '', '', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_termsconditions`
--

CREATE TABLE `realstateapp_termsconditions` (
  `id` bigint NOT NULL,
  `title` varchar(500) NOT NULL,
  `picture` varchar(100) NOT NULL,
  `terms_conditions` longtext NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_termsconditions`
--

INSERT INTO `realstateapp_termsconditions` (`id`, `title`, `picture`, `terms_conditions`, `status`) VALUES
(1, 'title', 'testimonial_image/terms-and-conditions.jpg', '<h2 style=\"text-align:justify\"><strong>TERMS &amp; CONDITIONS</strong></h2>\r\n\r\n<p style=\"text-align:justify\">These terms and conditions outline the rules and regulations for the use of STI Builders&#39;s Website.&nbsp;<br />\r\nSTI Builders is located at:</p>\r\n\r\n<p style=\"text-align:justify\"><strong>House#41 (Flat-A5,L-05), Sector#12, Uttara Model Town, Dhaka-1230</strong></p>\r\n\r\n<p style=\"text-align:justify\">By accessing this website, we assume you accept these terms and conditions in full. Do not continue to use Arisha&#39;s website if you do not accept all of the terms and conditions stated on this page.</p>\r\n\r\n<p style=\"text-align:justify\">The following terminology applies to these Terms and Conditions, Privacy Statement and Disclaimer Notice, and any or all Agreements: &quot;Client&quot;, &ldquo;You&rdquo; and &ldquo;Your&rdquo; refers to you, the person accessing this website and accepting the Company&rsquo;s terms and conditions. &quot;The Company&quot;, &ldquo;Ourselves&rdquo;, &ldquo;We&rdquo;, &ldquo;Our&rdquo; and &quot;Us&quot;, refers to our Company. &ldquo;Party&rdquo;, &ldquo;Parties&rdquo;, or &ldquo;Us&rdquo;, refers to both the Client and ourselves, or either the Client or ourselves. All terms refer to the offer, acceptance, and consideration of payment necessary to undertake the process of our assistance to the Client in the most appropriate manner, whether by formal meetings of a fixed duration or any other means, for the express purpose of meeting the Client&rsquo;s needs in respect of the provision of the Company&rsquo;s stated services/products, by and subject to, prevailing law of Bangladesh. Any use of the above terminology or other words in the singular, plural, capitalization, and/or he/she or they, are taken as interchangeable and therefore as referring to the same.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Cookies</strong></h3>\r\n\r\n<p style=\"text-align:justify\">We employ the use of cookies. By using&nbsp;<a href=\"https://www.stibuilderslimited.com/\">STI Builders</a>&#39;s website you consent to the use of cookies by&nbsp;<a href=\"https://www.stibuilderslimited.com/\">STI Builders</a>&#39;s privacy policy.</p>\r\n\r\n<p style=\"text-align:justify\">Most modern-day interactive websites use cookies to enable us to retrieve user details for each visit. Cookies are used in some areas of our site to enable the functionality of this area and ease of use for those people visiting. Some of our affiliate/advertising partners may also use cookies.</p>\r\n\r\n<h3 style=\"text-align:justify\">&nbsp;</h3>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Hyperlinking to our Content</strong></h3>\r\n\r\n<ol>\r\n	<li style=\"text-align: justify;\">The following organizations may link to our Web site without prior written approval:</li>\r\n</ol>\r\n\r\n<ul>\r\n	<li style=\"text-align: justify;\">Government agencies</li>\r\n	<li style=\"text-align: justify;\">Search engines</li>\r\n	<li style=\"text-align: justify;\">News organizations</li>\r\n	<li style=\"text-align: justify;\">Online directory distributors when they list us in the directory may link to our Web site in the same manner as they hyperlink to the Web sites of other listed businesses and</li>\r\n	<li style=\"text-align: justify;\">System-wide Accredited Businesses except soliciting non-profit organizations, charity shopping malls, and charity fundraising groups which may not hyperlink to our Web site.</li>\r\n</ul>\r\n\r\n<ol>\r\n	<li style=\"text-align: justify;\">These organizations may link to our home page, to publications, or other Web site information so long as the link: (a) is not in any way misleading; (b) does not falsely imply sponsorship, endorsement, or approval of the linking party and its products or services; and (c) fits within the context of the linking party&#39;s site.</li>\r\n	<li style=\"text-align: justify;\">We may consider and approve in our sole discretion other link requests from the following types of organizations:</li>\r\n</ol>\r\n\r\n<ul>\r\n	<li style=\"text-align: justify;\">com community sites</li>\r\n	<li style=\"text-align: justify;\">associations or other groups representing charities, including charity giving sites,</li>\r\n	<li style=\"text-align: justify;\">online directory distributors</li>\r\n	<li style=\"text-align: justify;\">internet portals</li>\r\n	<li style=\"text-align: justify;\">accounting, law, and consulting firms whose primary clients are businesses and</li>\r\n	<li style=\"text-align: justify;\">educational institutions and trade associations.</li>\r\n</ul>\r\n\r\n<p style=\"text-align:justify\">We will approve link requests from these organizations if we determine that: (a) the link would not reflect unfavorably on us or our accredited businesses (for example, trade associations or other organizations representing inherently suspect types of business, such as work-at-home opportunities, shall not be allowed to link); (b)the organization does not have an unsatisfactory record with us; (c) the benefit to us from the visibility associated with the hyperlink outweighs the absence of Arisha; and (d) where the link is in the context of general resource information or is otherwise consistent with editorial content in a newsletter or similar product furthering the mission of the organization.</p>\r\n\r\n<p style=\"text-align:justify\">These organizations may link to our home page, to publications, or other Web site information so long as the link: (a) is not in any way misleading; (b) does not falsely imply sponsorship, endorsement, or approval of the linking party and its products or services; and (c) fits within the context of the linking party&#39;s site.</p>\r\n\r\n<p style=\"text-align:justify\">If you are among the organizations listed in paragraph 2 above and are interested in linking to our website, you must notify us by sending an e-mail to&nbsp;<a href=\"mailto:stibuilders@gmail.com\">stibuilders@gmail.com</a>. Please include your name, your organization name, contact information (such as a phone number and/or e-mail address) as well as the URL of your site, a list of any URLs from which you intend to link to our Web site, and a list of the URL(s) on our site to which you would like to link. Allow 2-3 weeks for a response.</p>\r\n\r\n<p style=\"text-align:justify\">Approved organizations may hyperlink to our Web site as follows:</p>\r\n\r\n<ul>\r\n	<li style=\"text-align: justify;\">By use of our corporate name; or</li>\r\n	<li style=\"text-align: justify;\">By use of the uniform resource locator (Web address) being linked to; or</li>\r\n	<li style=\"text-align: justify;\">By use of any other description of our Web site or material being linked to that makes sense within the context and format of content on the linking party&#39;s site.</li>\r\n</ul>\r\n\r\n<p style=\"text-align:justify\">No use of (name)&rsquo;s logo or other artwork will be allowed for linking absent a trademark license agreement.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Content Liability</strong></h3>\r\n\r\n<p style=\"text-align:justify\">We shall have no responsibility or liability for any content appearing on your Web site. You agree to indemnify and defend us against all claims arising out of or based upon your Website. No link(s) may appear on any page on your Web site or within any context containing content or materials that may be interpreted as libelous, obscene, or criminal, or which infringes, otherwise violates, or advocates the infringement or other violation of, any third party rights.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Reservation of Rights</strong></h3>\r\n\r\n<p style=\"text-align:justify\">We reserve the right at any time and in its sole discretion to request that you remove all links or any particular link to our Web site. You agree to immediately remove all links to our Web site upon such request. We also reserve the right to amend these terms and conditions and its linking policy at any time. By continuing to link to our Web site, you agree to be bound to and abide by these linking terms and conditions.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Removal of links from our website</strong></h3>\r\n\r\n<p style=\"text-align:justify\">If you find any link on our Web site or any linked website objectionable for any reason, you may contact us about this. We will consider requests to remove links but will have no obligation to do so or to respond directly to you.</p>\r\n\r\n<p style=\"text-align:justify\">Whilst we endeavor to ensure that the information on this website is correct, we do not warrant its completeness or accuracy; nor do we commit to ensuring that the website remains available or that the material on the website is kept up to date.</p>\r\n\r\n<h3 style=\"text-align:justify\"><strong>Disclaimer</strong></h3>\r\n\r\n<p style=\"text-align:justify\">To the maximum extent permitted by applicable law, we exclude all representations, warranties, and conditions relating to our website and the use of this website (including, without limitation, any warranties implied by law in respect of satisfactory quality, fitness for purpose, and/or the use of reasonable care and skill). Nothing in this disclaimer will:</p>\r\n\r\n<ul>\r\n	<li style=\"text-align: justify;\">limit or exclude our or your liability for death or personal injury resulting from negligence</li>\r\n	<li style=\"text-align: justify;\">limit or exclude our or your liability for fraud or fraudulent misrepresentation</li>\r\n	<li style=\"text-align: justify;\">limit any of our or your liabilities in any way that is not permitted under applicable law or</li>\r\n	<li style=\"text-align: justify;\">exclude any of our or your liabilities that may not be excluded under applicable law.</li>\r\n</ul>\r\n\r\n<p style=\"text-align:justify\">The limitations and exclusions of liability set out in this Section and elsewhere in this disclaimer: (a) are subject to the preceding paragraph; and (b) govern all liabilities arising under the disclaimer or about the subject matter of this disclaimer, including liabilities arising in contract, in tort (including negligence) and for breach of statutory duty.</p>\r\n\r\n<p style=\"text-align:justify\">To the extent that the website and the information and services on the website are provided free of charge, we will not be liable for any loss or damage of any nature.</p>', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_testimonialadd`
--

CREATE TABLE `realstateapp_testimonialadd` (
  `id` bigint NOT NULL,
  `name` varchar(500) DEFAULT NULL,
  `profession` varchar(500) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `testimonial` longtext,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_testimonialadd`
--

INSERT INTO `realstateapp_testimonialadd` (`id`, `name`, `profession`, `image`, `testimonial`, `status`) VALUES
(1, NULL, 'Profession', 'testimonial_image/testimonial-1_Iq7iLh1.jpg', 'Our precious business partners, customers, and really valuable colleagues; will hold to work and produce to gain the future of our country. We will constantly keep our dreams at the best level to contribute to the economy and employment of our country, that\'s taking corporate steps toward becoming the world’s great power. Maintaining our determination on the road to our dreams ought to only be feasible with the value you added. Thank you very much for your belief in us.', 1),
(2, NULL, 'Profession', 'testimonial_image/testimonial-3_pVCG4gF.jpg', 'We have witnessed, by experiencing, that each work carried out with love, constantly looking after the good, can bring about success without dropping faith. Today, Arisha group is a big company serving in specific sectors which include construction, buildings, land share, engineering, and agro fisheries, and you, who take care of us and feel responsible, have a superb share in this.', 1);

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_testimonialvideo`
--

CREATE TABLE `realstateapp_testimonialvideo` (
  `id` bigint NOT NULL,
  `name` varchar(500) NOT NULL,
  `testimonial_video_url_link` varchar(1500) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `realstateapp_userregistrations`
--

CREATE TABLE `realstateapp_userregistrations` (
  `id` bigint NOT NULL,
  `full_name` varchar(256) NOT NULL,
  `user_mobile` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `user_password` varchar(256) NOT NULL,
  `date_of_birth` datetime(6) DEFAULT NULL,
  `address` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `user_type` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `realstateapp_userregistrations`
--

INSERT INTO `realstateapp_userregistrations` (`id`, `full_name`, `user_mobile`, `email`, `photo`, `user_password`, `date_of_birth`, `address`, `status`, `user_type`) VALUES
(1, 'Jahurul Islam', '01760960759', 'jahirbd360@gmail.com', 'images/user_photo/jahir_AboIqMv.jpg', '1234', '1995-12-02 12:00:00.000000', '  Kolabati, Sector-18,Uttara', 1, '1'),
(2, 'Mohammad Ismail', '01303101896', 'ismailnkbd@gmail.com', 'user_images/Ismail_bBadU0g.jpg', 'sti123', '1984-01-01 10:23:36.000000', '', 1, '1'),
(3, 'Sakib', '01322301173', '', '', '01322301173', NULL, ' ', 1, '2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `property_amenity`
--
ALTER TABLE `property_amenity`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_constructionstatus`
--
ALTER TABLE `property_constructionstatus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_facility`
--
ALTER TABLE `property_facility`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_landfacilityentry`
--
ALTER TABLE `property_landfacilityentry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_locationadd`
--
ALTER TABLE `property_locationadd`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_measurementscale`
--
ALTER TABLE `property_measurementscale`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_phaseadd`
--
ALTER TABLE `property_phaseadd`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_plotlandentry`
--
ALTER TABLE `property_plotlandentry`
  ADD PRIMARY KEY (`id`),
  ADD KEY `property_plotlandent_created_by_id_97c31999_fk_realstate` (`created_by_id`),
  ADD KEY `property_plotlandent_developer_name_id_53376aea_fk_property_` (`developer_name_id`),
  ADD KEY `property_plotlandent_measurement_scale_id_37fabd5b_fk_property_` (`measurement_scale_id`),
  ADD KEY `property_plotlandent_plot_land_status_id_44408f4b_fk_property_` (`plot_land_status_id`);

--
-- Indexes for table `property_plotlandfacility`
--
ALTER TABLE `property_plotlandfacility`
  ADD PRIMARY KEY (`id`),
  ADD KEY `property_plotlandfac_land_facility_id_bf38cb68_fk_property_` (`land_facility_id`);

--
-- Indexes for table `property_plotlandstatus`
--
ALTER TABLE `property_plotlandstatus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_projectadd`
--
ALTER TABLE `property_projectadd`
  ADD PRIMARY KEY (`id`),
  ADD KEY `property_projectadd_project_type_id_3dfad614_fk_property_` (`project_type_id`),
  ADD KEY `property_projectadd_created_by_id_1ce11667_fk_realstate` (`created_by_id`);

--
-- Indexes for table `property_projectplotland`
--
ALTER TABLE `property_projectplotland`
  ADD PRIMARY KEY (`id`),
  ADD KEY `property_projectplot_created_by_id_9d80e380_fk_realstate` (`created_by_id`);

--
-- Indexes for table `property_propertyamenity`
--
ALTER TABLE `property_propertyamenity`
  ADD PRIMARY KEY (`id`),
  ADD KEY `property_propertyame_amenity_name_id_d699a893_fk_property_` (`amenity_name_id`);

--
-- Indexes for table `property_propertyentry`
--
ALTER TABLE `property_propertyentry`
  ADD PRIMARY KEY (`id`),
  ADD KEY `property_propertyent_created_by_id_3cfc09f8_fk_realstate` (`created_by_id`);

--
-- Indexes for table `property_propertyfacility`
--
ALTER TABLE `property_propertyfacility`
  ADD PRIMARY KEY (`id`),
  ADD KEY `property_propertyfac_facility_name_id_ff0c6d49_fk_property_` (`facility_name_id`);

--
-- Indexes for table `property_propertyownership`
--
ALTER TABLE `property_propertyownership`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_propertyphoto`
--
ALTER TABLE `property_propertyphoto`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_propertytype`
--
ALTER TABLE `property_propertytype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_propertyvideo`
--
ALTER TABLE `property_propertyvideo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property_salesstatus`
--
ALTER TABLE `property_salesstatus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_affiliatesupplieradd`
--
ALTER TABLE `realstateapp_affiliatesupplieradd`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_certifiedadd`
--
ALTER TABLE `realstateapp_certifiedadd`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_chairmessage`
--
ALTER TABLE `realstateapp_chairmessage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_companyprofile`
--
ALTER TABLE `realstateapp_companyprofile`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_contactmessage`
--
ALTER TABLE `realstateapp_contactmessage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_eventgallery`
--
ALTER TABLE `realstateapp_eventgallery`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_faq`
--
ALTER TABLE `realstateapp_faq`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_hotnumber`
--
ALTER TABLE `realstateapp_hotnumber`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_privacypolicy`
--
ALTER TABLE `realstateapp_privacypolicy`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_qualityadd`
--
ALTER TABLE `realstateapp_qualityadd`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_servicedetails`
--
ALTER TABLE `realstateapp_servicedetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `realstateapp_service_service_name_id_e81d31fe_fk_realstate` (`service_name_id`);

--
-- Indexes for table `realstateapp_serviceentry`
--
ALTER TABLE `realstateapp_serviceentry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_sisternconcerndetails`
--
ALTER TABLE `realstateapp_sisternconcerndetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `realstateapp_sistern_sister_concern_name__e19f36a5_fk_realstate` (`sister_concern_name_id`);

--
-- Indexes for table `realstateapp_sisternconcernentry`
--
ALTER TABLE `realstateapp_sisternconcernentry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_sliderbanner`
--
ALTER TABLE `realstateapp_sliderbanner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_teammemberinfo`
--
ALTER TABLE `realstateapp_teammemberinfo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_termsconditions`
--
ALTER TABLE `realstateapp_termsconditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_testimonialadd`
--
ALTER TABLE `realstateapp_testimonialadd`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_testimonialvideo`
--
ALTER TABLE `realstateapp_testimonialvideo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `realstateapp_userregistrations`
--
ALTER TABLE `realstateapp_userregistrations`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=185;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `property_amenity`
--
ALTER TABLE `property_amenity`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `property_constructionstatus`
--
ALTER TABLE `property_constructionstatus`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `property_facility`
--
ALTER TABLE `property_facility`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `property_landfacilityentry`
--
ALTER TABLE `property_landfacilityentry`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `property_locationadd`
--
ALTER TABLE `property_locationadd`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `property_measurementscale`
--
ALTER TABLE `property_measurementscale`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `property_phaseadd`
--
ALTER TABLE `property_phaseadd`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `property_plotlandentry`
--
ALTER TABLE `property_plotlandentry`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `property_plotlandfacility`
--
ALTER TABLE `property_plotlandfacility`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `property_plotlandstatus`
--
ALTER TABLE `property_plotlandstatus`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `property_projectadd`
--
ALTER TABLE `property_projectadd`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `property_projectplotland`
--
ALTER TABLE `property_projectplotland`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `property_propertyamenity`
--
ALTER TABLE `property_propertyamenity`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104;

--
-- AUTO_INCREMENT for table `property_propertyentry`
--
ALTER TABLE `property_propertyentry`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `property_propertyfacility`
--
ALTER TABLE `property_propertyfacility`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `property_propertyownership`
--
ALTER TABLE `property_propertyownership`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=129;

--
-- AUTO_INCREMENT for table `property_propertyphoto`
--
ALTER TABLE `property_propertyphoto`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT for table `property_propertytype`
--
ALTER TABLE `property_propertytype`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `property_propertyvideo`
--
ALTER TABLE `property_propertyvideo`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=108;

--
-- AUTO_INCREMENT for table `property_salesstatus`
--
ALTER TABLE `property_salesstatus`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `realstateapp_affiliatesupplieradd`
--
ALTER TABLE `realstateapp_affiliatesupplieradd`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `realstateapp_certifiedadd`
--
ALTER TABLE `realstateapp_certifiedadd`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `realstateapp_chairmessage`
--
ALTER TABLE `realstateapp_chairmessage`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `realstateapp_companyprofile`
--
ALTER TABLE `realstateapp_companyprofile`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `realstateapp_contactmessage`
--
ALTER TABLE `realstateapp_contactmessage`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=115;

--
-- AUTO_INCREMENT for table `realstateapp_eventgallery`
--
ALTER TABLE `realstateapp_eventgallery`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `realstateapp_faq`
--
ALTER TABLE `realstateapp_faq`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `realstateapp_hotnumber`
--
ALTER TABLE `realstateapp_hotnumber`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `realstateapp_privacypolicy`
--
ALTER TABLE `realstateapp_privacypolicy`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `realstateapp_qualityadd`
--
ALTER TABLE `realstateapp_qualityadd`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `realstateapp_servicedetails`
--
ALTER TABLE `realstateapp_servicedetails`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `realstateapp_serviceentry`
--
ALTER TABLE `realstateapp_serviceentry`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `realstateapp_sisternconcerndetails`
--
ALTER TABLE `realstateapp_sisternconcerndetails`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `realstateapp_sisternconcernentry`
--
ALTER TABLE `realstateapp_sisternconcernentry`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `realstateapp_sliderbanner`
--
ALTER TABLE `realstateapp_sliderbanner`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `realstateapp_teammemberinfo`
--
ALTER TABLE `realstateapp_teammemberinfo`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `realstateapp_termsconditions`
--
ALTER TABLE `realstateapp_termsconditions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `realstateapp_testimonialadd`
--
ALTER TABLE `realstateapp_testimonialadd`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `realstateapp_testimonialvideo`
--
ALTER TABLE `realstateapp_testimonialvideo`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `realstateapp_userregistrations`
--
ALTER TABLE `realstateapp_userregistrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `property_plotlandentry`
--
ALTER TABLE `property_plotlandentry`
  ADD CONSTRAINT `property_plotlandentry_created_by_id_97c31999_fk` FOREIGN KEY (`created_by_id`) REFERENCES `realstateapp_userregistrations` (`id`),
  ADD CONSTRAINT `property_plotlandentry_developer_name_id_53376aea_fk` FOREIGN KEY (`developer_name_id`) REFERENCES `property_projectplotland` (`id`),
  ADD CONSTRAINT `property_plotlandentry_measurement_scale_id_37fabd5b_fk` FOREIGN KEY (`measurement_scale_id`) REFERENCES `property_measurementscale` (`id`),
  ADD CONSTRAINT `property_plotlandentry_plot_land_status_id_44408f4b_fk` FOREIGN KEY (`plot_land_status_id`) REFERENCES `property_plotlandstatus` (`id`);

--
-- Constraints for table `property_plotlandfacility`
--
ALTER TABLE `property_plotlandfacility`
  ADD CONSTRAINT `property_plotlandfacility_land_facility_id_bf38cb68_fk` FOREIGN KEY (`land_facility_id`) REFERENCES `property_landfacilityentry` (`id`);

--
-- Constraints for table `property_projectadd`
--
ALTER TABLE `property_projectadd`
  ADD CONSTRAINT `property_projectadd_created_by_id_1ce11667_fk` FOREIGN KEY (`created_by_id`) REFERENCES `realstateapp_userregistrations` (`id`),
  ADD CONSTRAINT `property_projectadd_project_type_id_3dfad614_fk` FOREIGN KEY (`project_type_id`) REFERENCES `property_propertytype` (`id`);

--
-- Constraints for table `property_projectplotland`
--
ALTER TABLE `property_projectplotland`
  ADD CONSTRAINT `property_projectplotland_created_by_id_9d80e380_fk` FOREIGN KEY (`created_by_id`) REFERENCES `realstateapp_userregistrations` (`id`);

--
-- Constraints for table `property_propertyamenity`
--
ALTER TABLE `property_propertyamenity`
  ADD CONSTRAINT `property_propertyamenity_amenity_name_id_d699a893_fk` FOREIGN KEY (`amenity_name_id`) REFERENCES `property_amenity` (`id`);

--
-- Constraints for table `property_propertyentry`
--
ALTER TABLE `property_propertyentry`
  ADD CONSTRAINT `property_propertyentry_created_by_id_3cfc09f8_fk` FOREIGN KEY (`created_by_id`) REFERENCES `realstateapp_userregistrations` (`id`);

--
-- Constraints for table `property_propertyfacility`
--
ALTER TABLE `property_propertyfacility`
  ADD CONSTRAINT `property_propertyfacility_facility_name_id_ff0c6d49_fk` FOREIGN KEY (`facility_name_id`) REFERENCES `property_facility` (`id`);

--
-- Constraints for table `realstateapp_servicedetails`
--
ALTER TABLE `realstateapp_servicedetails`
  ADD CONSTRAINT `realstateapp_servicedetails_service_name_id_e81d31fe_fk` FOREIGN KEY (`service_name_id`) REFERENCES `realstateapp_serviceentry` (`id`);

--
-- Constraints for table `realstateapp_sisternconcerndetails`
--
ALTER TABLE `realstateapp_sisternconcerndetails`
  ADD CONSTRAINT `realstateapp_sisternconce_sister_concern_name_id_e19f36a5_fk` FOREIGN KEY (`sister_concern_name_id`) REFERENCES `realstateapp_sisternconcernentry` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
