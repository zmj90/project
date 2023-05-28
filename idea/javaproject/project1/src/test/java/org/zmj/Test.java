package org.zmj;

import com.alibaba.fastjson.JSONArray;

import java.sql.SQLException;

public class Test {
    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        String[] array = {"UPDATE customers SET cust_country = '中国' WHERE cust_id IN (10005, 10004)", "UPDATE customers SET cust_country = '中国' WHERE cust_id IN (10005, 10004)", "SELECT * FROM `customers`"};
        JSONArray resultFromMysql = ConMysql.getResultFromMysql("localhost", "3307", "test2", "root", "123456", array);
        System.out.println(resultFromMysql);
    }
}
