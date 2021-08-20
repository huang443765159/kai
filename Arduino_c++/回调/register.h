#ifndef REGISTER_H
#define REGISTER_H


class Test
{
    typedef void (*conn_cb)(const u_int8_t, bool);   //声明一个回调函数  后面要传递几个参数就写几个参数
    public:
        test();
        void register_callback_conn(conn_cb func);  //回调函数
        void update();
    private:
        u_int8_t _id;
        bool _ena;
        // CALLBACK
        conn_cb _conn_cb;
};

extern Test test; // 生成类的单例

#endif;