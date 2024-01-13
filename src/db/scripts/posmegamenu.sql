CREATE TABLE IF NOT EXISTS `ps_posmegamenu_item` (
    `id_posmegamenu_item` int(11) NOT NULL AUTO_INCREMENT,
	`type_link` int(10) unsigned NOT NULL,
	`link` varchar(255) NULL,
	`type_icon` int(10) unsigned NULL,
	`icon` varchar(255) NULL,
	`icon_class` text NULL,
	`submenu_type` int(10) NULL,
	`item_class` varchar(255) NULL,
	`new_window` tinyint(1) unsigned,
	`position` int(10) unsigned NOT NULL DEFAULT '0',
	`active` tinyint(1) unsigned NOT NULL DEFAULT '0',
	`item_bg_color` varchar(64) NULL,
	`item_bg_colorh` varchar(64) NULL,
	`item_color` varchar(64) NULL,
    `item_colorh` varchar(64) NULL,
    `item_fontsize` tinyint(1) unsigned NULL,
    `item_lineheight` tinyint(1) unsigned NULL,
    `item_transform` tinyint(1) unsigned NULL,
    `subtitle_bg_color` varchar(64) NULL,
    `subtitle_color` varchar(64) NULL,
    `subtitle_fontsize` tinyint(1) unsigned NULL,
    `subtitle_lineheight` tinyint(1) unsigned NULL,
    `subtitle_transform` tinyint(1) unsigned NULL,
    PRIMARY KEY  (`id_posmegamenu_item`) 
   );
   
   
delete from `ps_posmegamenu_item`;
INSERT INTO `ps_posmegamenu_item` (`id_posmegamenu_item`, `type_link`, `link`, `type_icon`, `icon`, `icon_class`, `submenu_type`, `item_class`, `new_window`, `position`, `active`, `item_bg_color`, `item_bg_colorh`, `item_color`, `item_colorh`, `item_fontsize`, `item_lineheight`, `item_transform`, `subtitle_bg_color`, `subtitle_color`, `subtitle_fontsize`, `subtitle_lineheight`, `subtitle_transform`) VALUES
(3, 0, 'CAT3373', 0, NULL, NULL, 0, NULL, 0, 0, 1, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0),
(4, 0, 'CAT3227', 0, NULL, NULL, 0, NULL, 0, 1, 1, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0),
(5, 0, 'CAT5453', 0, NULL, NULL, 0, NULL, 0, 2, 1, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0),
(6, 1, NULL, 0, NULL, NULL, 0, NULL, 0, 4, 1, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0),
(7, 0, 'CAT3228', 0, NULL, NULL, 0, NULL, 0, 3, 1, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0),
(8, 1, NULL, 0, NULL, NULL, 0, NULL, 0, 5, 1, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0);


CREATE TABLE IF NOT EXISTS `ps_posmegamenu_item_lang` (
	  `id_posmegamenu_item` int(10) unsigned NOT NULL AUTO_INCREMENT,
	  `id_lang` int(10) unsigned NOT NULL,
	  `title` varchar(255) NULL,
	  `custom_link` varchar(255) NULL,
	  `subtitle` varchar(255) NULL,
	  PRIMARY KEY (`id_posmegamenu_item`, `id_lang`)
	) ;

delete from `ps_posmegamenu_item_lang`;
INSERT INTO `ps_posmegamenu_item_lang` (`id_posmegamenu_item`, `id_lang`, `title`, `custom_link`, `subtitle`) VALUES
(3, 1, 'Cellphones', '#', NULL),
(3, 2, 'סמארטםונים', '#', NULL),
(3, 7, 'Телефоны', '#', NULL),
(4, 1, 'Tablet computers', '#', NULL),
(4, 2, 'מחשב קף יד', '#', NULL),
(4, 7, 'Планшетные компьютеры', '#', NULL),
(5, 1, 'Laptops', '#', NULL),
(5, 2, 'מחשבים ניידים', '#', NULL),
(5, 7, 'Лептопы', '#', NULL),
(6, 1, 'Smart', '#', NULL),
(6, 2, 'סמארט', '#', NULL),
(6, 7, 'Смарт', '#', NULL),
(7, 1, 'Gaming consoles', '#', NULL),
(7, 2, 'קונסולות משחק', '#', NULL),
(7, 7, 'Игровые приставки', '#', NULL),
(8, 1, 'Sound', '#', NULL),
(8, 2, 'שמע', '#', NULL),
(8, 7, 'Звук', '#', NULL);


CREATE TABLE IF NOT EXISTS `ps_posmegamenu_item_shop` 
(
    `id_posmegamenu_item` int(11) NOT NULL AUTO_INCREMENT,
	`id_shop` int(10) unsigned NOT NULL,
    PRIMARY KEY  (`id_posmegamenu_item`, `id_shop`)
) ;
delete from `ps_posmegamenu_item_shop`;
INSERT INTO `ps_posmegamenu_item_shop` (`id_posmegamenu_item`, `id_shop`) VALUES
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1);

CREATE TABLE IF NOT EXISTS `ps_posmegamenu_submenu` (
	  `id_submenu` int(10) unsigned NOT NULL AUTO_INCREMENT,
	  `id_posmegamenu_item` int(10) unsigned NOT NULL,
	  `submenu_class` varchar(64) NULL,
	  `active` tinyint(1) unsigned NOT NULL DEFAULT '0',
	  `submenu_width` tinyint(1) unsigned NULL,
	  `submenu_bg` varchar(64) NULL,
	  `submenu_bg_color` varchar(64) NULL,
	  `submenu_bg_image` varchar(255) NULL,
	  `submenu_bg_repeat` tinyint(1) unsigned NULL,
	  `submenu_bg_position` tinyint(1) unsigned NULL,
	  `submenu_link_color` varchar(64) NULL,
	  `submenu_link_colorh` varchar(64) NULL,
	  `submenu_link_fontsize` tinyint(1) unsigned NULL,
	  `submenu_link_lineheight` tinyint(1) unsigned NULL,
	  `submenu_link_transform` tinyint(1) unsigned NULL,
	  `submenu_title_color` varchar(64) NULL,
	  `submenu_title_colorh` varchar(64) NULL,
	  `submenu_title_fontsize` tinyint(1) unsigned NULL,
	  `submenu_title_lineheight` tinyint(1) unsigned NULL,
	  `submenu_title_transform` tinyint(1) unsigned NULL,

	  PRIMARY KEY (`id_submenu`)
	) ;
delete from `ps_posmegamenu_submenu`;
INSERT INTO `ps_posmegamenu_submenu` (`id_submenu`, `id_posmegamenu_item`, `submenu_class`, `active`, `submenu_width`, `submenu_bg`, `submenu_bg_color`, `submenu_bg_image`, `submenu_bg_repeat`, `submenu_bg_position`, `submenu_link_color`, `submenu_link_colorh`, `submenu_link_fontsize`, `submenu_link_lineheight`, `submenu_link_transform`, `submenu_title_color`, `submenu_title_colorh`, `submenu_title_fontsize`, `submenu_title_lineheight`, `submenu_title_transform`) VALUES
(2, 2, NULL, 1, 12, '1', NULL, NULL, 1, 1, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0),
(3, 3, NULL, 1, 12, '1', NULL, NULL, 1, 1, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0),
(4, 4, NULL, 1, 6, '1', NULL, NULL, 1, 1, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0),
(5, 5, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(6, 6, NULL, 1, 12, '1', NULL, NULL, 1, 1, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0),
(7, 7, NULL, 1, 12, '1', NULL, NULL, 1, 1, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0),
(8, 8, NULL, 1, 12, '1', NULL, NULL, 1, 1, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0);



CREATE TABLE IF NOT EXISTS `ps_posmegamenu_submenu_column` (
	  `id_posmegamenu_submenu_column` int(10) unsigned NOT NULL AUTO_INCREMENT,
	  `id_row` int(10) unsigned NOT NULL,
	  `width` varchar(255) NULL,
	  `class` varchar(64) NULL,
	  `type_link` int(10) unsigned NULL,
	  `link` varchar(64) NULL,
	  `position` int(10) unsigned NOT NULL DEFAULT '0',
	  `active_mobile` tinyint(1) unsigned NOT NULL DEFAULT '0',
	  `active` tinyint(1) unsigned NOT NULL DEFAULT '0',
	  PRIMARY KEY (`id_posmegamenu_submenu_column`)
	)  ;
delete from `ps_posmegamenu_submenu_column`;
INSERT INTO `ps_posmegamenu_submenu_column` (`id_posmegamenu_submenu_column`, `id_row`, `width`, `class`, `type_link`, `link`, `position`, `active_mobile`, `active`) VALUES
(1, 1, '12', NULL, 0, 'PAGhomepage', 1, 1, 1),
(4, 2, '2', NULL, 0, 'CAT6273', 1, 1, 1),
(5, 2, '2', NULL, 0, 'CAT3418', 0, 1, 1),
(6, 2, '2', NULL, 0, 'CAT4771', 3, 1, 1),
(7, 2, '2', NULL, 0, 'CAT3400', 2, 1, 1),
(8, 2, '2', NULL, 0, 'CAT3403', 4, 1, 1),
(9, 2, '2', NULL, 0, 'CAT6338', 5, 1, 1),
(12, 6, '2', NULL, 0, 'CAT3228', 6, 1, 1),
(13, 6, '2', NULL, 0, 'CAT3391', 7, 1, 1),
(14, 5, '4', NULL, 0, 'CAT6430', 8, 1, 1),
(15, 5, '4', NULL, 0, 'CAT6429', 9, 1, 1),
(16, 5, '4', NULL, 0, 'CAT6432', 10, 1, 1);


CREATE TABLE IF NOT EXISTS `ps_posmegamenu_submenu_column_lang` (
	  `id_posmegamenu_submenu_column` int(10) unsigned NOT NULL AUTO_INCREMENT,
	  `title` varchar(64) NULL,
	  `custom_link` varchar(64) NULL,
	  `id_lang` int(10) unsigned NOT NULL,
	  PRIMARY KEY (`id_posmegamenu_submenu_column`,`id_lang`)
	)  ;
delete from `ps_posmegamenu_submenu_column_lang`;

INSERT INTO `ps_posmegamenu_submenu_column_lang` 
(`id_posmegamenu_submenu_column`, `title`, `custom_link`, `id_lang`) VALUES
(1, NULL, NULL, 1),
(1, NULL, NULL, 2),
(1, NULL, NULL, 7),
(4, NULL, NULL, 1),
(4, NULL, NULL, 2),
(4, NULL, NULL, 7),
(5, NULL, NULL, 1),
(5, NULL, NULL, 2),
(5, NULL, NULL, 7),
(6, NULL, NULL, 1),
(6, NULL, NULL, 2),
(6, NULL, NULL, 7),
(7, NULL, NULL, 1),
(7, NULL, NULL, 2),
(7, NULL, NULL, 7),
(8, NULL, NULL, 1),
(8, NULL, NULL, 2),
(8, NULL, NULL, 7),
(9, NULL, NULL, 1),
(9, NULL, NULL, 2),
(9, NULL, NULL, 7),
(12, NULL, NULL, 1),
(12, NULL, NULL, 2),
(12, NULL, NULL, 7),
(13, NULL, NULL, 1),
(13, NULL, NULL, 2),
(13, NULL, NULL, 7),
(14, NULL, NULL, 1),
(14, NULL, NULL, 2),
(14, NULL, NULL, 7),
(15, NULL, NULL, 1),
(15, NULL, NULL, 2),
(15, NULL, NULL, 7),
(16, NULL, NULL, 1),
(16, NULL, NULL, 2),
(16, NULL, NULL, 7);

CREATE TABLE IF NOT EXISTS `ps_posmegamenu_submenu_item` (
    `id_posmegamenu_submenu_item` int(11) NOT NULL AUTO_INCREMENT,
    `id_posmegamenu_submenu_column` int(11) unsigned NOT NULL,
	`type_link` int(10) unsigned NULL,
	`category_tree` varchar(64) NULL,
	`ps_link` varchar(64) NULL,	
	`id_product` int(10) unsigned DEFAULT NULL,
	`id_manufacturer` int(10) unsigned DEFAULT NULL,
	`position` int(10) unsigned NOT NULL DEFAULT '0',
	`active_mobile` tinyint(1) unsigned NOT NULL DEFAULT '0',
	`active` tinyint(1) unsigned NOT NULL DEFAULT '0',
    PRIMARY KEY  (`id_posmegamenu_submenu_item`)
)  ;
delete from `ps_posmegamenu_submenu_item`;
INSERT INTO `ps_posmegamenu_submenu_item` (`id_posmegamenu_submenu_item`, `id_posmegamenu_submenu_column`, `type_link`, `category_tree`, `ps_link`, `id_product`, `id_manufacturer`, `position`, `active_mobile`, `active`) VALUES
(1, 1, 6, NULL, 'PAGhomepage', 0, 2, 1, 1, 1),
(4, 4, 1, 'CAT6273', 'PAGhomepage', 0, 5651, 2, 1, 1),
(5, 5, 1, 'CAT3418', 'PAGhomepage', 0, 5651, 3, 1, 1),
(6, 6, 1, 'CAT4771', 'PAGhomepage', 0, 5651, 2, 1, 1),
(7, 7, 1, 'CAT3400', 'PAGhomepage', 0, 5651, 5, 1, 1),
(8, 8, 1, 'CAT3403', 'PAGhomepage', 0, 5651, 6, 1, 1),
(9, 9, 1, 'CAT6338', 'PAGhomepage', 0, 5651, 7, 1, 1),
(11, 9, 1, 'CAT4790', 'PAGhomepage', 0, 5651, 9, 1, 1),
(12, 7, 1, 'CAT6189', 'PAGhomepage', 0, 5651, 10, 1, 1),
(13, 8, 1, 'CAT6190', 'PAGhomepage', 0, 5651, 11, 1, 1),
(14, 6, 1, 'CAT6191', 'PAGhomepage', 0, 5651, 1, 1, 1),
(15, 4, 1, 'CAT6201', 'PAGhomepage', 0, 5651, 12, 1, 1),
(16, 8, 1, 'CAT6368', 'PAGhomepage', 0, 5651, 13, 1, 1),
(17, 8, 1, 'CAT6370', 'PAGhomepage', 0, 5651, 14, 1, 1),
(18, 7, 1, 'CAT6321', 'PAGhomepage', 0, 5651, 15, 1, 1),
(19, 6, 1, 'CAT6372', 'PAGhomepage', 0, 5651, 0, 1, 1),
(20, 12, 1, 'CAT3376', 'PAGhomepage', 0, 5651, 16, 1, 1),
(21, 13, 1, 'CAT3391', 'PAGhomepage', 0, 5651, 17, 1, 1),
(22, 4, 1, 'CAT6375', 'PAGhomepage', 0, 5651, 18, 1, 1),
(23, 4, 1, 'CAT6428', 'PAGhomepage', 0, 5651, 19, 1, 1),
(24, 14, 1, 'CAT6430', 'PAGhomepage', 0, 5651, 20, 1, 1),
(25, 15, 1, 'CAT6429', 'PAGhomepage', 0, 5651, 21, 1, 1),
(26, 16, 1, 'CAT6431', 'PAGhomepage', 0, 5651, 22, 1, 1);

CREATE TABLE IF NOT EXISTS `ps_posmegamenu_submenu_item_lang` (
	  `id_posmegamenu_submenu_item` int(10) unsigned NOT NULL AUTO_INCREMENT,
	  `id_lang` int(10) unsigned NOT NULL,
	  `customlink_title` varchar(64) NULL,
	  `customlink_link` varchar(64) NULL,
	  `htmlcontent` text NULL,
	  `image` varchar(255) NULL,
	  `image_link` varchar(255) NULL,
	  PRIMARY KEY (`id_posmegamenu_submenu_item`, `id_lang`)
	)  ;
delete from `ps_posmegamenu_submenu_item_lang`;
INSERT INTO `ps_posmegamenu_submenu_item_lang` (`id_posmegamenu_submenu_item`, `id_lang`, `customlink_title`, `customlink_link`, `htmlcontent`, `image`, `image_link`) VALUES
(1, 1, NULL, NULL, NULL, NULL, NULL),
(4, 1, NULL, NULL, NULL, NULL, NULL),
(4, 2, NULL, NULL, NULL, NULL, NULL),
(4, 7, NULL, NULL, NULL, NULL, NULL),
(5, 1, NULL, NULL, NULL, NULL, NULL),
(5, 2, NULL, NULL, NULL, NULL, NULL),
(5, 7, NULL, NULL, NULL, NULL, NULL),
(6, 1, NULL, NULL, NULL, NULL, NULL),
(6, 2, NULL, NULL, NULL, NULL, NULL),
(6, 7, NULL, NULL, NULL, NULL, NULL),
(7, 1, NULL, NULL, NULL, NULL, NULL),
(7, 2, NULL, NULL, NULL, NULL, NULL),
(7, 7, NULL, NULL, NULL, NULL, NULL),
(8, 1, NULL, NULL, NULL, NULL, NULL),
(8, 2, NULL, NULL, NULL, NULL, NULL),
(8, 7, NULL, NULL, NULL, NULL, NULL),
(9, 1, NULL, NULL, NULL, NULL, NULL),
(9, 2, NULL, NULL, NULL, NULL, NULL),
(9, 7, NULL, NULL, NULL, NULL, NULL),
(11, 1, NULL, NULL, NULL, NULL, NULL),
(11, 2, NULL, NULL, NULL, NULL, NULL),
(11, 7, NULL, NULL, NULL, NULL, NULL),
(12, 1, NULL, NULL, NULL, NULL, NULL),
(12, 2, NULL, NULL, NULL, NULL, NULL),
(12, 7, NULL, NULL, NULL, NULL, NULL),
(13, 1, NULL, NULL, NULL, NULL, NULL),
(13, 2, NULL, NULL, NULL, NULL, NULL),
(13, 7, NULL, NULL, NULL, NULL, NULL),
(14, 1, NULL, NULL, NULL, NULL, NULL),
(14, 2, NULL, NULL, NULL, NULL, NULL),
(14, 7, NULL, NULL, NULL, NULL, NULL),
(15, 1, NULL, NULL, NULL, NULL, NULL),
(15, 2, NULL, NULL, NULL, NULL, NULL),
(15, 7, NULL, NULL, NULL, NULL, NULL),
(16, 1, NULL, NULL, NULL, NULL, NULL),
(16, 2, NULL, NULL, NULL, NULL, NULL),
(16, 7, NULL, NULL, NULL, NULL, NULL),
(17, 1, NULL, NULL, NULL, NULL, NULL),
(17, 2, NULL, NULL, NULL, NULL, NULL),
(17, 7, NULL, NULL, NULL, NULL, NULL),
(18, 1, NULL, NULL, NULL, NULL, NULL),
(18, 2, NULL, NULL, NULL, NULL, NULL),
(18, 7, NULL, NULL, NULL, NULL, NULL),
(19, 1, NULL, NULL, NULL, NULL, NULL),
(19, 2, NULL, NULL, NULL, NULL, NULL),
(19, 7, NULL, NULL, NULL, NULL, NULL),
(20, 1, NULL, NULL, NULL, NULL, NULL),
(20, 2, NULL, NULL, NULL, NULL, NULL),
(20, 7, NULL, NULL, NULL, NULL, NULL),
(21, 1, NULL, NULL, NULL, NULL, NULL),
(21, 2, NULL, NULL, NULL, NULL, NULL),
(21, 7, NULL, NULL, NULL, NULL, NULL),
(22, 1, NULL, NULL, NULL, NULL, NULL),
(22, 2, NULL, NULL, NULL, NULL, NULL),
(22, 7, NULL, NULL, NULL, NULL, NULL),
(23, 1, NULL, NULL, NULL, NULL, NULL),
(23, 2, NULL, NULL, NULL, NULL, NULL),
(23, 7, NULL, NULL, NULL, NULL, NULL),
(24, 1, NULL, NULL, NULL, NULL, NULL),
(24, 2, NULL, NULL, NULL, NULL, NULL),
(24, 7, NULL, NULL, NULL, NULL, NULL),
(25, 1, NULL, NULL, NULL, NULL, NULL),
(25, 2, NULL, NULL, NULL, NULL, NULL),
(25, 7, NULL, NULL, NULL, NULL, NULL),
(26, 1, NULL, NULL, NULL, NULL, NULL),
(26, 2, NULL, NULL, NULL, NULL, NULL),
(26, 7, NULL, NULL, NULL, NULL, NULL);



CREATE TABLE IF NOT EXISTS `ps_posmegamenu_submenu_row` (
	  `id_row` int(10) unsigned NOT NULL AUTO_INCREMENT,
	  `id_posmegamenu_item` int(10) unsigned NOT NULL,
	  `class` varchar(255) NULL,
	  `position` int(10) unsigned NOT NULL DEFAULT '0',
	  `active` tinyint(1) unsigned NOT NULL DEFAULT '0',
	  PRIMARY KEY (`id_row`)
	)  ;
delete from `ps_posmegamenu_submenu_row`;
INSERT INTO `ps_posmegamenu_submenu_row` (`id_row`, `id_posmegamenu_item`, `class`, `position`, `active`) VALUES
(1, 2, NULL, 1, 1),
(2, 3, NULL, 2, 1),
(5, 6, NULL, 3, 1),
(6, 7, NULL, 4, 1),
(7, 8, NULL, 5, 1);


