-- u782528968_Erx8s.wxrq_product_lang definition

CREATE TABLE `wxrq_product_lang` (
  `id_product` int(10) unsigned NOT NULL,
  `id_shop` int(11) unsigned NOT NULL DEFAULT 1,
  `id_lang` int(10) unsigned NOT NULL,
  `description` text DEFAULT NULL,
  `description_short` text DEFAULT NULL,
  `link_rewrite` varchar(128) NOT NULL,
  `meta_description` varchar(512) DEFAULT NULL,
  `meta_keywords` varchar(256) DEFAULT NULL,
  `meta_title` varchar(256) DEFAULT NULL,
  `name` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `available_now` varchar(256) DEFAULT NULL,
  `available_later` varchar(256) DEFAULT NULL,
  `delivery_in_stock` varchar(256) DEFAULT NULL,
  `delivery_out_stock` varchar(256) DEFAULT NULL,
  `affiliate_short_link` varchar(256) DEFAULT NULL,
  `affiliate_text` mediumtext DEFAULT NULL,
  `affiliate_summary` mediumtext DEFAULT NULL,
  `affiliate_summary_2` mediumtext DEFAULT NULL,
  `ingridients` tinytext DEFAULT NULL,
  `how_to_use` tinytext DEFAULT NULL COMMENT 'нструкция по использованию товара',
  `additional_shipping_message` tinytext DEFAULT NULL COMMENT 'Дополнительное сообщение к условиям отправки',
  PRIMARY KEY (`id_product`,`id_shop`,`id_lang`),
  KEY `id_lang` (`id_lang`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;