package org.zmj;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class ConMysql {
    public static JSONArray getResultFromMysql(String host, String port, String database, String user, String password, String[] sqls) throws ClassNotFoundException, SQLException {
        // 加载驱动
        Class.forName("com.mysql.cj.jdbc.Driver");
        // 连接数据库返回数据库对象
        String url = "jdbc:mysql://" + host + ":" + port + "/" + database + "?useUnicode=true&characterEnoding=utf8&useSSL=true";
        Connection connection = DriverManager.getConnection(url, user, password);
        connection.setAutoCommit(false);
        // 创建执行sql对象
        Statement statement = connection.createStatement();
        for (String sql :
                sqls) {
            statement.addBatch(sql);
            System.out.println(sql);
        }
        try {
            int[] ints = statement.executeBatch();
            connection.commit();
            JSONArray array = new JSONArray();
            for (int i = 0; i < ints.length; i++) {
                array.add(i, ints[i]);
            }
            return array;
        } catch (Exception e) {
            connection.rollback();
            return JSON.parseArray("[111]");
        } finally {
            statement.close();
            connection.close();
        }
    }
}