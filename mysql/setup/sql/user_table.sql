CREATE TABLE IF NOT EXISTS `database`.`user` (
    `id` int(10) NOT NULL AUTO_INCREMENT,
    `first_name` varchar(255) NOT NULL,
    `last_name` varchar(255) NOT NULL,
    `email` varchar(255) NOT NULL,
    `gender` varchar(10) NOT NULL,
    `record_date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `record_date_last_modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;
