--建立微信后台处理表
DROP TABLE public."B_WX_USERS";
CREATE TABLE public."B_WX_USERS"
(
   "ID" character varying(32),
   "USER_CODE" character varying(100),
   "USER_NAME" character varying(100),
   "USER_PASS" character varying(128),
   "USER_PHONE" character varying(15),
   "USER_SEX" character varying(1),
   "USER_AGE" int,
   "USER_ADDRESS" character varying(200),
   "USER_EMAIL" character varying(40),
   CONSTRAINT "B_WX_USERS_PK" PRIMARY KEY ("ID")
)
WITH (
  OIDS = FALSE
)
;
COMMENT ON COLUMN public."B_WX_USERS"."ID" IS '主键';
COMMENT ON COLUMN public."B_WX_USERS"."USER_CODE" IS '用户登录账号，SYSADMIN为管理员账号';
COMMENT ON COLUMN public."B_WX_USERS"."USER_NAME" IS '用户名称';
COMMENT ON COLUMN public."B_WX_USERS"."USER_PASS" IS '用户密码，采用32位DES加密';
COMMENT ON COLUMN public."B_WX_USERS"."USER_PHONE" IS '用户联系方式';
COMMENT ON COLUMN public."B_WX_USERS"."USER_SEX" IS '用户姓别';
COMMENT ON COLUMN public."B_WX_USERS"."USER_AGE" IS '用户年龄';
COMMENT ON COLUMN public."B_WX_USERS"."USER_ADDRESS" IS '用户通信地址';
COMMENT ON COLUMN public."B_WX_USERS"."USER_EMAIL" IS '用户邮件';
COMMENT ON TABLE public."B_WX_USERS"
  IS '用户表，用于管理用户接入平台情况';
INSERT INTO public."B_WX_USERS"(
            "ID", "USER_CODE", "USER_NAME", "USER_PASS", "USER_PHONE", "USER_SEX",
            "USER_AGE", "USER_ADDRESS", "USER_EMAIL")
    VALUES('abcdefghgi','SYSADMIN','管理员','f6235735d47e6ccc82cc743bb0f4578e2f21572003d61e62c719fd9345101031e6aeed4b2ba8b059916b3764dac90fbdb6a0a88fe5fa7d7f483013a63cc089e0',NULL ,NULL ,0,NULL,'zhguokai@163.com');

--初始化自定义消息回复
