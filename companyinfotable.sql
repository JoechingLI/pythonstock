/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50726
Source Host           : localhost:3306
Source Database       : stock_db

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2021-07-28 16:52:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `companyinfotable`
-- ----------------------------
DROP TABLE IF EXISTS `companyinfotable`;
CREATE TABLE `companyinfotable` (
  `ts_code` varchar(255) NOT NULL,
  `exchange` varchar(255) DEFAULT NULL,
  `chairman` varchar(255) DEFAULT NULL,
  `manager` varchar(255) DEFAULT NULL,
  `secretary` varchar(255) DEFAULT NULL,
  `reg_capital` varchar(255) DEFAULT NULL,
  `setup_date` varchar(255) DEFAULT NULL,
  `province` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `introduction` varchar(3000) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `office` varchar(255) DEFAULT NULL,
  `employees` varchar(255) DEFAULT NULL,
  `main_business` varchar(1000) DEFAULT NULL,
  `business_scope` varchar(3000) DEFAULT NULL,
  PRIMARY KEY (`ts_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of companyinfotable
-- ----------------------------
