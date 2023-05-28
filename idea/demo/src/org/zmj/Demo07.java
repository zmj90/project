package org.zmj;

import java.sql.*;

public class Demo01 {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        // 1 加载驱动
        Class.forName("com.mysql.cj.jdbc.Driver");
        // 2 用户信息和url
        String url = "jdbc:mysql://localhost:3306/test?useUnicode=true&characterEnoding=utf8&useSSL=true";
        String username = "root";
        String password = "123456";
        // 3 连接数据库返回数据库对象
        Connection connection = DriverManager.getConnection(url, username, password);
        // 4 创建执行sql对象
        Statement statement = connection.createStatement();
        // 5 执行sql
        String sql = "SELECT * FROM customers";

//        ResultSet resultSet = statement.executeQuery(sql);
        ResultSet resultSet = statement.executeQuery(sql);

        while (resultSet.next()){
            System.out.println("cust_id=" + resultSet.getObject("cust_id"));
            System.out.println("cust_name=" + resultSet.getObject("cust_name"));
            System.out.println("cust_address=" + resultSet.getObject("cust_address"));
        }
        // 6 释放资源
        resultSet.close();
        statement.close();
        connection.close();
    }


}
