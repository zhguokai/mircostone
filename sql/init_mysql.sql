/***
  用于描述初始化脚本
*/
-- 初始化数据库
DROP DATABASE IF EXISTS `mircostone`;
CREATE DATABASE `mircostone` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `mircostone`;
-- 初始化用户表
DROP TABLE IF EXISTS `b_wx_users`;
CREATE TABLE `b_wx_users` (
  `user_id`      VARCHAR(36)
                 COLLATE utf8_unicode_ci NOT NULL
  COMMENT '主键',
  `user_code`    VARCHAR(45)
                 COLLATE utf8_unicode_ci DEFAULT NULL
  COMMENT '用户编号，系统惟一，用于登录系统',
  `user_name`    VARCHAR(45)
                 COLLATE utf8_unicode_ci DEFAULT NULL
  COMMENT '用户名称，注册用户信息',
  `user_pass`    VARCHAR(128)
                 COLLATE utf8_unicode_ci DEFAULT NULL
  COMMENT '用户密码，采用SHA512加密',
  `user_email`   VARCHAR(50)
                 COLLATE utf8_unicode_ci DEFAULT NULL
  COMMENT '用户邮件',
  `user_phone`   VARCHAR(15)
                 COLLATE utf8_unicode_ci DEFAULT NULL
  COMMENT '用户联系方式，定义为手机号',
  `user_type`    VARCHAR(4)
                 COLLATE utf8_unicode_ci DEFAULT NULL
  COMMENT '用户类型1管理员、2订阅号(未认证)、3订阅号（认证）、3服务号（未认证）、4服务号（认证）、5企业号（未认证）、6企业号（认证）、7开发者测试号',
  `user_address` VARCHAR(300)
                 COLLATE utf8_unicode_ci DEFAULT NULL
  COMMENT '用户联系地址',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `idb_wx_users_UNIQUE` (`user_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COLLATE = utf8_unicode_ci
  COMMENT = '用户信息表,用于存储微石系统的用户';

-- 增加管理员用户
INSERT INTO `mircostone`.`b_wx_users`
(`user_id`, `user_code`, `user_name`, `user_pass`, `user_email`, `user_phone`, `user_type`, `user_address`)
VALUES ('sysadmin', 'sysadmin', '管理员',
        'f6235735d47e6ccc82cc743bb0f4578e2f21572003d61e62c719fd9345101031e6aeed4b2ba8b059916b3764dac90fbdb6a0a88fe5fa7d7f483013a63cc089e0',
        'cppzgk@163.com', '13988881234', '1', '北京市宣武区');
