from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clazz` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '班级名称'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '姓名',
    `pwd` VARCHAR(32) NOT NULL COMMENT '密码',
    `sno` INT NOT NULL COMMENT '学号',
    `clazz_id` INT NOT NULL,
    CONSTRAINT `fk_student_clazz_cff127e1` FOREIGN KEY (`clazz_id`) REFERENCES `clazz` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '教师姓名',
    `pwd` VARCHAR(32) NOT NULL COMMENT '密码',
    `tno` INT NOT NULL COMMENT '教师号'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '课程名称',
    `teacher_id` INT NOT NULL,
    CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_course` (
    `student_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cou_student_0d222b` (`student_id`, `course_id`)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
