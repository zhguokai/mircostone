/**
 * 摇一摇处理方法，调用devicemotion方法
 **/


//定义事件捕捉器
/**
 * 定义全局的属性
 * **/

// 首先，定义一个摇动的阀值
var SHAKE_THRESHOLD = 1000;
// 定义一个变量保存上次更新的时间
var last_update = 0;
// 紧接着定义x、y、z记录三个轴的数据以及上一次出发的时间
var x = 0, y = 0, z = 0;

var last_x = 0, last_y = 0, last_z = 0;
var length = 0;
function deviceMotionHandler(eventData) {

    // 获取含重力的加速度
    var acceleration = eventData.accelerationIncludingGravity;
    // 获取当前时间
    var curTime = new Date().getTime();
    var diffTime = curTime - last_update;

    // 固定时间段
    if (diffTime > 50) {
        last_update = curTime;
        x = acceleration.x;
        y = acceleration.y;
        z = acceleration.z;
        var speed = Math.abs(x + y + z - last_x - last_y - last_z) / diffTime * 10000;
        length += Math.abs(x + y + z - last_x - last_y - last_z) / 3;
        if (speed > 500) {
            //设置动态摇晃图
            $("#wxcq_cq").css("display", "block");
            //使晃动的速度与距离都达到要求时,抽出结果签来展示
            if (speed > SHAKE_THRESHOLD && length > 50) {
                //重新设置Length
                length = 0;
                //手机震动
                navigator.vibrate(1000);
                //显示结果
                showResultImg();
                return;
            }
        }
        last_x = x;
        last_y = y;
        last_z = z;
    }
}


/**
 * 展示抽签结果
 * */
var showResultImg = function () {
     $("#wxcq_cq").css("display", "none");
    $("#result").css("display", "block");
    $("#result_yq").css("display", "block");
    //处理重新抽签的方式
}
/**
 * 提交当前表单数据
 * */
var subData = function () {
    //定义当前系统标识
    $("#cqjg_cur_time").val(new Date().getTime());
    $("#wxcqForm")[0].submit();
}
