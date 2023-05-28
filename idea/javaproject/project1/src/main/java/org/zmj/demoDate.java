package org.zmj;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class demoDate {
    public static void main(String[] args) {
//        Calendar instance = Calendar.getInstance();
//        Calendar instance1 = Calendar.getInstance();
//        instance.add(5, 10);
//        SimpleDateFormat sdf = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
//        String format = sdf.format(instance.getTime());
//        String format1 = sdf.format(instance1.getTime());
//        System.out.println(format);
//        System.out.println(format1);
        Date dNow = new Date( );
        SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd hh:mm:ss");
        String format = ft.format(dNow);
        System.out.println("当前时间为: " + ft.format(dNow));
        System.out.println(dNow.getTime());
        long l = dNow.getTime() + 10 * 60 * 1000;
        System.out.println(l);
        dNow.setTime(l);
        String format1 = ft.format(dNow);
        System.out.println(format);
        System.out.println(format1);
        System.out.println(ft.toPattern());

    }
}
