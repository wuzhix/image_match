'''
CREATE TABLE `goods_cat` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `parentid` int(10) NOT NULL DEFAULT '0' COMMENT '父类id',
  `catid` int(10) unsigned NOT NULL COMMENT '分类id',
  `catname` varchar(50) NOT NULL DEFAULT '' COMMENT '分类名称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `goods_pic` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `sa_id` bigint(20) unsigned NOT NULL COMMENT '图片id',
  `pic` varchar(255) NOT NULL DEFAULT '' COMMENT '图片url',
  `one` smallint(5) unsigned NOT NULL DEFAULT '0' COMMENT '图片一级分类',
  `two` smallint(5) unsigned NOT NULL DEFAULT '0' COMMENT '图片二级分类',
  `three` smallint(5) unsigned NOT NULL DEFAULT '0' COMMENT '图片三级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
from django.db import models


# Create your models here.
class Cat(models.Model):
    class Meta:
        db_table = 'goods_cat'
    cat = models.IntegerField(db_column='catid')
    parent = models.IntegerField(db_column='parentid')
    name = models.CharField(db_column='catname', max_length=50)


class Pic(models.Model):
    class Meta:
        db_table = 'goods_pic'
    sa_id = models.BigIntegerField(db_column='sa_id')
    pic = models.CharField(db_column='pic', max_length=255)
    one = models.IntegerField(db_column='one')
    two = models.IntegerField(db_column='two')
    three = models.IntegerField(db_column='three')
