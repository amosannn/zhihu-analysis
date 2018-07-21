/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50722
 Source Host           : localhost:3306
 Source Schema         : scrapy

 Target Server Type    : MySQL
 Target Server Version : 50722
 File Encoding         : 65001

 Date: 21/07/2018 11:16:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zhihu_user
-- ----------------------------
DROP TABLE IF EXISTS `zhihu_user`;
CREATE TABLE `zhihu_user`  (
  `user_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '',
  `sex` int(4) NULL DEFAULT -1,
  `user_sign` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '',
  `user_avatar` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '',
  `user_url` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '',
  `locations` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '',
  `voteup_count` int(10) NULL DEFAULT 0,
  `thanked_Count` int(10) NULL DEFAULT 0,
  `follower_count` int(10) NULL DEFAULT 0,
  `following_count` int(10) NULL DEFAULT 0,
  `following_topic_count` int(10) NULL DEFAULT 0,
  `following_question_count` int(10) NULL DEFAULT 0,
  `following_favlists_count` int(10) NULL DEFAULT 0,
  `following_columns_count` int(10) NULL DEFAULT 0,
  `answer_count` int(10) NULL DEFAULT 0,
  `articles_count` int(10) NULL DEFAULT 0,
  `question_count` int(10) NULL DEFAULT 0,
  `commercial_question_count` int(10) NULL DEFAULT 0,
  `favorite_count` int(10) NULL DEFAULT 0,
  `favorited_count` int(10) NULL DEFAULT 0,
  `is_bind_sina` int(4) NULL DEFAULT 0,
  `is_following` int(10) NULL DEFAULT 0,
  `is_followed` tinyint(1) NULL DEFAULT 0,
  `mutual_followees_count` int(10) NULL DEFAULT 0,
  `vote_to_count` int(10) NULL DEFAULT 0,
  `vote_from_count` int(10) NULL DEFAULT 0,
  `thank_to_count` int(10) NULL DEFAULT 0,
  `thank_from_count` int(10) NULL DEFAULT 0,
  `description` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '',
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
