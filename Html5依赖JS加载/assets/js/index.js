// ---------- 可配置项 ----------

// 风险提示的文字
var text_tips = '关好车窗\n拉好手刹\n不要移动\n~';

// 清洗步骤的文字
var text_wash = [
    '轮毂清洗',
    '车身清洗',
    '高压冲水',
    '水蜡处理',
    '低压冲水',
    '烘干处理'
];

// 完成时的提示文字
var text_finish = 'Oh Yeah\n去闪亮登场吧';

//命令集合
var commands = [
    'screen_saver',//screen_saver:无人时显示的屏保动画，全屏幕金色泡泡
    'entrance_door_open',//entrance_door_open:入场⻔打开，泡泡开始向左下⻆偏移，并出现问候语
    'entrance_door_opened',//entrance_door_opened:入场⻔完全打开，显示向前滚动箭头
    'arrows_change1',// arrows_change1:箭头变色，频率加快x1
    'arrows_change2',// arrows_change2:箭头变色，频率加快x2
    'arrows_change3',// arrows_change3:箭头变色，频率加快x3
        'car_back',// car_back:显示向下缓慢移动的红色箭头
        'long_car',//long_car:车辆超出清洗范围，请离开。
    'stop_driving',// stop_driving:停止行驶，显示stop界面
    'risk_warning',// risk_warning:⻛险提示。
    'countdown',// countdown:3.2.1倒计时动画
    'washing1',// washing1:清洗⻚面，第1个步骤。
    'washing2',// washing2:清洗⻚面，第2个步骤。
    'washing3',// washing3:清洗⻚面，第3个步骤。
    'washing4',// washing4:清洗⻚面，第4个步骤。
    'washing5',// washing5:清洗⻚面，第5个步骤。
    'washing6',// washing6:清洗⻚面，第6个步骤。
    'wash_finished',// wash_finished:清洗完成⻚面。
    'car_leave',// car_leave:离开⻚面，Bye那个⻚面
        'please_leave_soon',// please_leave_soon:请尽快离场⻚面
        'customer_service',// customer_service:呼叫人工客服⻚面
    'reload'// reload:刷新页面
];






//循环时间线
var tl = new TimelineMax({repeat:-1, repeatDelay:2});
var tl1 = new TimelineMax({repeat:-1, repeatDelay:2});
var tl2 = new TimelineMax({repeat:-1, repeatDelay:0});
var tl3 = new TimelineMax({repeat:-1, repeatDelay:2});
var tl_arrow = new TimelineMax({repeat:-1, repeatDelay:0});
//驱动动画，command为指令
function go(command) {

    if (commands.indexOf(command) == -1) {
        alert('跳转指令不存在');
        return;
    }

    switch (command) {
        case 'screen_saver':
            
            if (currentCommand == 'screen_saver') {
                currentCommand = 'screen_saver';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                stage.addChild(spriteDatas.hi.ooo);
                stage.removeChild(spriteDatas.drive.ooo);
                stage.removeChild(spriteDatas.tips.ooo);
                stage.removeChild(spriteDatas.countDown.ooo);
                stage.removeChild(spriteDatas.wash.ooo);
                stage.removeChild(spriteDatas.finish.ooo);
                

                var pop = spriteDatas.hi.children.pop.ooo;
                var eyes = spriteDatas.hi.children.pop.children.eyes.ooo;
                var eye_l = spriteDatas.hi.children.pop.children.eyes.children.l.ooo;
                var eye_r = spriteDatas.hi.children.pop.children.eyes.children.r.ooo;
                
                //复位
                /* pop.alpha = 1;
                pop.scale.set(1,1);
                pop.x = spriteDatas.hi.children.pop.x;
                pop.y = spriteDatas.hi.children.pop.y; */


                pop.scale.set(1.55, 1.55);
                pop.x = pop.x-1000;
                pop.y = pop.y-1000;
                eyes.x = eyes.x - 40;
                eyes.y = eyes.y + 300;

                tl.to(eyes, 0.2, {x:'-=40'});
                tl.staggerTo([eye_l, eye_r], 0.1, {width:66, height:6, delay:0.2});
                tl.staggerTo([eye_l, eye_r], 0.1, {width:60, height:62});
                tl.staggerTo([eye_l, eye_r], 0.1, {width:66, height:6});
                tl.staggerTo([eye_l, eye_r], 0.1, {width:60, height:62});

                tl.to(eyes, 0.2, {x:'+=40', delay:2});
                tl.staggerTo([eye_l, eye_r], 0.1, {width:66, height:6, delay:0.2});
                tl.staggerTo([eye_l, eye_r], 0.1, {width:60, height:62});
                tl.staggerTo([eye_l, eye_r], 0.1, {width:66, height:6});
                tl.staggerTo([eye_l, eye_r], 0.1, {width:60, height:62});
            } else {
                alert('当时位置不能跳转到 screen_saver');
            }
        break;



        case 'entrance_door_open':
            if (currentCommand == 'screen_saver') {
                currentCommand = 'entrance_door_open';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                // tl.to(pop, 0.5, {x:'-=20'});
                var pop = spriteDatas.hi.children.pop.ooo;
                var eyes = spriteDatas.hi.children.pop.children.eyes.ooo;
                var eye_r = spriteDatas.hi.children.pop.children.eyes.children.r.ooo;
                var eye_r2 = spriteDatas.hi.children.pop.children.eyes.children.r2.ooo;
                var bubble = spriteDatas.hi.children.bubble.ooo;

                TweenMax.to(pop.scale, 0.7, {x:1, y:1, overwrite:1, ease:Cubic.easeOut});
                TweenMax.to(pop, 0.7, {x:-1420, y:395, overwrite:1, ease:Cubic.easeOut});
                setTimeout(() => {
                    eye_r.visible = false;
                    eye_r2.visible = true;
                }, 300);

                TweenMax.to(eyes, 0.5, {x:1755, y:671, overwrite:1, ease:Power3.easeOut});

                TweenMax.to(bubble, 0.5, {alpha:1, overwrite:1, delay:0.3});
                TweenMax.to(bubble.scale, 0.5, {x:1, y:1, ease:Back.easeOut, overwrite:1, delay:0.3});

            } else {
                alert('当时位置不能跳转到 entrance_door_open');
            }
        break;



        case 'entrance_door_opened':
            if (currentCommand == 'entrance_door_open') {
                currentCommand = 'entrance_door_opened';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------


                var bubble = spriteDatas.hi.children.bubble.ooo;
                var pop = spriteDatas.hi.children.pop.ooo;
                TweenMax.to(bubble.scale, 0.5, {x:0, y:0, ease:Back.easeIn, overwrite:1});
                TweenMax.to(pop, 0.8, {x:-1420-2000, y:395-200, overwrite:1, ease:Power1.easeInOut, delay:0.2, onComplete:function(){
                    stage.removeChild(spriteDatas.hi.ooo);
                }});

                // spriteDatas.drive.ooo.x += 2000;
                // TweenMax.to(spriteDatas.drive.ooo, 1, {x:spriteDatas.drive.ooo.x-2000, overwrite:1, ease:Power1.easeInOut, delay:0.2});
                TweenMax.from(spriteDatas.drive.ooo, 0.4, {alpha:0, overwrite:1, delay:0.8});
                stage.addChild(spriteDatas.drive.ooo);

                var arrows = spriteDatas.drive.children.arrowsC.children.arrows.ooo;
                // tl.clear();
                // tl.repeatDelay(0);
                tl_arrow.fromTo(arrows, 0.35, {y:0, ease:Linear.easeOut}, {y:-1500, ease:Linear.easeOut});
                // tl.to(arrows, 0, {y:arrows.y+1500});

                
            } else {
                alert('当时位置不能跳转到 entrance_door_opened');
            }
        break;



        case 'arrows_change1':
            if (currentCommand == 'entrance_door_opened') {
                currentCommand = 'arrows_change1';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                tl_arrow.timeScale(0.5);
                var arrow1 = spriteDatas.drive.children.arrowsC.children.arrows.children.arrow1.ooo;
                var arrow2 = spriteDatas.drive.children.arrowsC.children.arrows.children.arrow2.ooo;
                var arrow3 = spriteDatas.drive.children.arrowsC.children.arrows.children.arrow3.ooo;
                arrow1.texture = textures.s2['arrow_2.png'];
                arrow2.texture = textures.s2['arrow_2.png'];
                arrow3.texture = textures.s2['arrow_2.png'];
                /* var children = tl.getChildren(false, true, true, 0);
                var tm = children[0];
                var tt = tm.time();
                tm.duration(0.5);
                tm.time(tt); */
            } else {
                alert('当时位置不能跳转到 arrows_change1');
            }
        break;



        case 'arrows_change2':
            if (currentCommand == 'arrows_change1') {
                currentCommand = 'arrows_change2';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                tl_arrow.timeScale(0.25);
                var arrow1 = spriteDatas.drive.children.arrowsC.children.arrows.children.arrow1.ooo;
                var arrow2 = spriteDatas.drive.children.arrowsC.children.arrows.children.arrow2.ooo;
                var arrow3 = spriteDatas.drive.children.arrowsC.children.arrows.children.arrow3.ooo;
                arrow1.texture = textures.s2['arrow_3.png'];
                arrow2.texture = textures.s2['arrow_3.png'];
                arrow3.texture = textures.s2['arrow_3.png'];
                /* var children = tl.getChildren(false, true, true, 0);
                var tm = children[0];
                var tt = tm.time();
                tm.duration(0.8);
                tm.time(tt); */
            } else {
                alert('当时位置不能跳转到 arrows_change2');
            }
        break;



        case 'arrows_change3':
            if (currentCommand == 'arrows_change2') {
                currentCommand = 'arrows_change3';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                tl_arrow.timeScale(0.125);
                var arrow1 = spriteDatas.drive.children.arrowsC.children.arrows.children.arrow1.ooo;
                var arrow2 = spriteDatas.drive.children.arrowsC.children.arrows.children.arrow2.ooo;
                var arrow3 = spriteDatas.drive.children.arrowsC.children.arrows.children.arrow3.ooo;
                arrow1.texture = textures.s2['arrow_4.png'];
                arrow2.texture = textures.s2['arrow_4.png'];
                arrow3.texture = textures.s2['arrow_4.png'];
                /* var children = tl.getChildren(false, true, true, 0);
                var tm = children[0];
                var tt = tm.time();
                tm.duration(1.2);
                tm.time(tt); */
            } else if (currentCommand == 'car_back') {
                currentCommand = 'arrows_change3';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                tl_arrow.timeScale(0.125);
                var arrowsC = spriteDatas.drive.children.arrowsC.ooo;
                arrowsC.scale.y = 1;

            } else if (currentCommand == 'stop_driving' || currentCommand == 'risk_warning' || currentCommand == 'countdown') {
                

                if (currentCommand == 'stop_driving') {
                    var stop = spriteDatas.drive.children.stop.ooo;
                    TweenMax.to(stop, 0.3, {y:1024-300, alpha:0, ease:Cubic.easeOut, overwrite:1});
                }
                if (currentCommand == 'risk_warning') {
                    TweenMax.to(spriteDatas.tips.ooo, 0.4, {alpha:0, overwrite:1});
                }
                if (currentCommand == 'countdown') {
                    TweenMax.to(spriteDatas.countDown.ooo, 0.4, {alpha:0, overwrite:1});
                }


                currentCommand = 'arrows_change3';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------


                var arrowsC = spriteDatas.drive.children.arrowsC.ooo;
                TweenMax.to(arrowsC, 0.4, {alpha:1, overwrite:1});
                arrowsC.scale.y = 1;

            } else {
                alert('当时位置不能跳转到 arrows_change3');
            }
        break;



        case 'car_back':
            if (currentCommand == 'arrows_change3') {
                currentCommand = 'car_back';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                tl_arrow.timeScale(0.125);
                var arrowsC = spriteDatas.drive.children.arrowsC.ooo;
                arrowsC.scale.y = -1;
            } else if (currentCommand == 'stop_driving' || currentCommand == 'risk_warning' || currentCommand == 'countdown') {
                

                if (currentCommand == 'stop_driving') {
                    var stop = spriteDatas.drive.children.stop.ooo;
                    TweenMax.to(stop, 0.3, {y:1024-300, alpha:0, ease:Cubic.easeOut, overwrite:1});
                }
                if (currentCommand == 'risk_warning') {
                    TweenMax.to(spriteDatas.tips.ooo, 0.4, {alpha:0, overwrite:1});
                }
                if (currentCommand == 'countdown') {
                    TweenMax.to(spriteDatas.countDown.ooo, 0.4, {alpha:0, overwrite:1});
                }

                currentCommand = 'car_back';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                var arrowsC = spriteDatas.drive.children.arrowsC.ooo;
                TweenMax.to(arrowsC, 0.4, {alpha:1, overwrite:1});
                arrowsC.scale.y = -1;

            } else {
                alert('当时位置不能跳转到 car_back');
            }
        break;



        case 'long_car':
            if (currentCommand == 'arrows_change3') {
                currentCommand = 'long_car';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                var arrows = spriteDatas.drive.children.arrowsC.children.arrows.ooo;
                TweenMax.to(arrows, 0.4, {alpha:0, overwrite:1});





                var ccc = spriteDatas.finish.children.ccc.ooo;
                var text = spriteDatas.finish.children.text.ooo;
                ccc.visible = false;
                text.visible = false;

                var face1 = spriteDatas.finish.children.pop.children.face1.ooo;
                var face2 = spriteDatas.finish.children.pop.children.face2.ooo;
                var face3 = spriteDatas.finish.children.pop.children.face3.ooo;
                face1.visible = false;
                face2.visible = false;
                face3.visible = false;

                var longcar = spriteDatas.finish.children.longcar.ooo;
                longcar.visible = true;
                TweenMax.from(longcar, 0.4, {alpha:0, x:longcar.x + 600, ease:Cubic.easeOut, overwrite:1, delay:0.6});


                var face4 = spriteDatas.finish.children.pop.children.face4.ooo;
                face4.visible = true;
                TweenMax.from(face4, 0.5, {alpha:0, ease:Linear.easeOut, overwrite:1, delay:0.1});


                var pop = spriteDatas.finish.children.pop.ooo;
                var pop_body = spriteDatas.finish.children.pop.children.body.ooo;
                pop_body.texture = PIXI.loader.resources['assets/images/scene/textures/popBody_Gray.png'].texture;



                pop.y = 1235 + 1600;
                TweenMax.to(pop.scale, 0.7, {x:1520/332, y:1520/332, ease:Back.easeOut, overwrite:1, delay:0});
                TweenMax.to(pop, 0.7, {x:687, y:1235, ease:Back.easeOut, overwrite:1, delay:0, onComplete:()=>{
                    tl1.clear();
                    tl1.repeatDelay(0);
                    tl1.yoyo(false);
                    // tl1.to(pop, 2, {x:'-=50'});
                    // tl1.to(pop, 0.2, {x:'-=50'});
                    tl1.to(pop, 0.05, {x:'+=10', delay:2});
                    tl1.to(pop, 0.05, {x:'-=10'});
                    tl1.to(pop, 0.05, {x:'+=10'});
                    tl1.to(pop, 0.05, {x:'-=10'});
                    tl1.to(pop, 0.05, {x:'+=10'});
                    tl1.to(pop, 0.05, {x:'-=10'});
                    tl1.to(pop, 0.05, {x:'+=10'});
                    tl1.to(pop, 0.05, {x:'-=10'});
                    tl1.to(pop, 0.05, {x:'+=10'});
                    tl1.to(pop, 0.05, {x:'-=10'});
                }});


                
                


                stage.addChild(spriteDatas.finish.ooo);

                

            } else {
                alert('当时位置不能跳转到 long_car');
            }
        break;



        case 'stop_driving':
            if (currentCommand == 'arrows_change3' || currentCommand == 'car_back') {
                currentCommand = 'stop_driving';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                /* var arrows = spriteDatas.drive.children.arrowsC.children.arrows.ooo;
                TweenMax.to(arrows, 0.4, {alpha:0, overwrite:1, onComplete:function(){
                    // tl.clear();
                }}); */
                var arrowsC = spriteDatas.drive.children.arrowsC.ooo;
                TweenMax.to(arrowsC, 0.4, {alpha:0, overwrite:1});

                var stop = spriteDatas.drive.children.stop.ooo;
                stop.visible = true;
                TweenMax.fromTo(stop, 0.4, {y:1024+600, alpha:0, ease:Cubic.easeOut, overwrite:1}, {y:1024, alpha:1, ease:Cubic.easeOut, overwrite:1});

            } else {
                alert('当时位置不能跳转到 stop_driving');
            }
        break;



        case 'risk_warning':
            if (currentCommand == 'stop_driving') {
                currentCommand = 'risk_warning';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                var stop = spriteDatas.drive.children.stop.ooo;
                TweenMax.to(stop, 0.3, {alpha:0, ease:Linear.easeOut, overwrite:1});
                
                TweenMax.fromTo(spriteDatas.tips.ooo, 0.5, {alpha:0, overwrite:1}, {alpha:1, overwrite:1});
                TweenMax.fromTo(spriteDatas.tips.ooo.scale, 0.5, {x:0, y:0, ease:Back.easeOut, overwrite:1}, {x:1, y:1, ease:Back.easeOut, overwrite:1});
                /* TweenMax.fromTo(spriteDatas.tips.ooo.scale, 0.5, {x:0, y:0, ease:Back.easeOut, overwrite:1, onComplete:function(){
                    stage.removeChild(spriteDatas.drive.ooo);
                }}); */
                stage.addChild(spriteDatas.tips.ooo);



            } else {
                alert('当时位置不能跳转到 risk_warning');
            }
        break;



        case 'countdown':
            if (currentCommand == 'risk_warning') {
                currentCommand = 'countdown';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                TweenMax.to(spriteDatas.tips.ooo, 0.4, {alpha:0, overwrite:1});
                TweenMax.to(spriteDatas.tips.ooo.scale, 0.4, {x:0, y:0, ease:Cubic.easeOut, overwrite:1});

                stage.addChild(spriteDatas.countDown.ooo);
                TweenMax.to(spriteDatas.countDown.ooo, 0.4, {alpha:1, overwrite:1});
                var n1 = spriteDatas.countDown.children.n1.ooo;
                var n2 = spriteDatas.countDown.children.n2.ooo;
                var n3 = spriteDatas.countDown.children.n3.ooo;
                n1.scale.set(0,0);
                n2.scale.set(0,0);
                n3.scale.set(0,0);
                n1.alpha = 1;
                n2.alpha = 2;
                n3.alpha = 3;

                TweenMax.to(n1.scale, 0.5, {x:1, y:1, ease:Back.easeOut, overwrite:1, delay:2, onComplete:function(){
                    TweenMax.to(n1.scale, 1, {x:3, y:3, ease:Cubic.easeOut, overwrite:1});
                    TweenMax.to(n1, 1, {alpha:0, overwrite:1});
                }});
                TweenMax.to(n2.scale, 0.5, {x:1, y:1, ease:Back.easeOut, overwrite:1, delay:1, onComplete:function(){
                    TweenMax.to(n2.scale, 1, {x:3, y:3, ease:Cubic.easeOut, overwrite:1});
                    TweenMax.to(n2, 1, {alpha:0, overwrite:1});
                }});
                TweenMax.to(n3.scale, 0.5, {x:1, y:1, ease:Back.easeOut, overwrite:1, delay:0, onComplete:function(){
                    TweenMax.to(n3.scale, 1, {x:3, y:3, ease:Cubic.easeOut, overwrite:1});
                    TweenMax.to(n3, 1, {alpha:0, overwrite:1});
                }});


            } else {
                alert('当时位置不能跳转到 countdown');
            }
        break;



        case 'washing1':
            if (currentCommand == 'countdown') {
                currentCommand = 'washing1';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------
                
                TweenMax.to(spriteDatas.countDown.ooo, 0.4, {alpha:0, overwrite:1, onComplete:function(){
                    stage.removeChild(spriteDatas.countDown.ooo);
                }});
                TweenMax.from(spriteDatas.wash.ooo, 0.4, {alpha:0, overwrite:1});
                stage.addChild(spriteDatas.wash.ooo);

                var ccc = spriteDatas.wash.children.cc.children.ccc.ooo;
                tl.clear();
                tl.repeatDelay(0);
                tl.timeScale(1);
                tl.fromTo(ccc, 2, {rotation:0, ease:Linear.easeOut}, {rotation:Math.PI*2, ease:Linear.easeOut});

            } else {
                alert('当时位置不能跳转到 washing1');
            }
        break;



        case 'washing2':
            if (currentCommand == 'washing1') {
                currentCommand = 'washing2';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------
                
                var step = spriteDatas.wash.children.cc.children.step.ooo;
                step.texture = textures.s1['step_2.png'];
                var text = spriteDatas.wash.children.text.ooo;
                text.text = text_wash[1];

            } else {
                alert('当时位置不能跳转到 washing2');
            }
        break;



        case 'washing3':
            if (currentCommand == 'washing2') {
                currentCommand = 'washing3';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                var step = spriteDatas.wash.children.cc.children.step.ooo;
                step.texture = textures.s1['step_3.png'];
                var text = spriteDatas.wash.children.text.ooo;
                text.text = text_wash[2];
                
            } else {
                alert('当时位置不能跳转到 washing3');
            }
        break;



        case 'washing4':
            if (currentCommand == 'washing3') {
                currentCommand = 'washing4';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                var step = spriteDatas.wash.children.cc.children.step.ooo;
                step.texture = textures.s1['step_4.png'];
                var text = spriteDatas.wash.children.text.ooo;
                text.text = text_wash[3];
                
            } else {
                alert('当时位置不能跳转到 washing4');
            }
        break;



        case 'washing5':
            if (currentCommand == 'washing4') {
                currentCommand = 'washing5';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                var step = spriteDatas.wash.children.cc.children.step.ooo;
                step.texture = textures.s1['step_5.png'];
                var text = spriteDatas.wash.children.text.ooo;
                text.text = text_wash[4];
                
            } else {
                alert('当时位置不能跳转到 washing5');
            }
        break;



        case 'washing6':
            if (currentCommand == 'washing5') {
                currentCommand = 'washing6';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                var step = spriteDatas.wash.children.cc.children.step.ooo;
                step.texture = textures.s1['step_6.png'];
                var text = spriteDatas.wash.children.text.ooo;
                text.text = text_wash[5];
                // text.
                // text.align = 'center';
            } else {
                alert('当时位置不能跳转到 washing6');
            }
        break;



        case 'wash_finished':
            if (currentCommand == 'washing6') {
                currentCommand = 'wash_finished';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                TweenMax.to(spriteDatas.wash.ooo, 0.4, {alpha:0, overwrite:1, onComplete:function(){
                    stage.removeChild(spriteDatas.wash.ooo);
                }});

                var ccc = spriteDatas.finish.children.ccc.ooo;
                var text = spriteDatas.finish.children.text.ooo;
                var pop = spriteDatas.finish.children.pop.ooo;

                TweenMax.from(pop.scale, 0.8, {x:0, y:0, ease:Back.easeOut, overwrite:1});
                TweenMax.from(text, 0.5, {y:text.y+600, ease:Cubic.easeOut, overwrite:1});
                TweenMax.from(ccc, 0.5, {alpha:0, overwrite:1});
                stage.addChild(spriteDatas.finish.ooo);




                var face1 = spriteDatas.finish.children.pop.children.face1.ooo;
                var eye_l = spriteDatas.finish.children.pop.children.face1.children.eyeL.ooo;
                var eye_r = spriteDatas.finish.children.pop.children.face1.children.eyeR.ooo;

                

                // var tl1 = new TimelineMax({repeat:-1, repeatDelay:2});
                tl1.to(face1, 0.2, {x:'-=50'});
                tl1.staggerTo([eye_l, eye_r], 0.1, {width:19+2, height:2, delay:0.2});
                tl1.staggerTo([eye_l, eye_r], 0.1, {width:19, height:18});
                tl1.staggerTo([eye_l, eye_r], 0.1, {width:19+2, height:2});
                tl1.staggerTo([eye_l, eye_r], 0.1, {width:19, height:18});

                tl1.to(face1, 0.2, {x:'+=50', delay:2});
                tl1.staggerTo([eye_l, eye_r], 0.1, {width:18.6+2, height:2, delay:0.2});
                tl1.staggerTo([eye_l, eye_r], 0.1, {width:18.6, height:18});
                tl1.staggerTo([eye_l, eye_r], 0.1, {width:18.6+2, height:2});
                tl1.staggerTo([eye_l, eye_r], 0.1, {width:18.6, height:18});


                tl2.yoyo(true);
                tl2.to(ccc.scale, 0.5, {x:1.08, y:1.08});


                /* setTimeout(() => {
                    
                }, 800); */

            } else {
                alert('当时位置不能跳转到 wash_finished');
            }
        break;



        case 'car_leave':
            if (currentCommand == 'wash_finished') {
                currentCommand = 'car_leave';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------

                var ccc = spriteDatas.finish.children.ccc.ooo;
                var text = spriteDatas.finish.children.text.ooo;
                var pop = spriteDatas.finish.children.pop.ooo;
                TweenMax.to(ccc, 0.5, {alpha:0, overwrite:1});
                TweenMax.to(text, 0.5, {y:text.y+600, alpha:0, ease:Cubic.easeIn, overwrite:1});
                TweenMax.to(pop.scale, 1, {x:1520/332, y:1520/332, ease:Cubic.easeOut, overwrite:1, delay:0.5});
                TweenMax.to(pop, 1, {x:687, y:1235, ease:Cubic.easeOut, overwrite:1, delay:0.5, onComplete:()=>{
                    // var tl2 = new TimelineMax({repeat:-1, repeatDelay:0, yoyo:true});
                    tl1.clear();
                    tl1.repeatDelay(0);
                    tl1.yoyo(true);
                    tl1.to(pop, 2, {y:'-=80'});

                    var eye_l = spriteDatas.finish.children.pop.children.face2.children.eyeL.ooo;
                    var eye_r = spriteDatas.finish.children.pop.children.face2.children.eyeR.ooo;

                    tl3.staggerTo([eye_l, eye_r], 0.1, {width:10, height:2});
                    tl3.staggerTo([eye_l, eye_r], 0.1, {width:8.5, height:8.8});
                    tl3.staggerTo([eye_l, eye_r], 0.1, {width:10, height:2});
                    tl3.staggerTo([eye_l, eye_r], 0.1, {width:8.5, height:8.8});
                }});

                var bye = spriteDatas.finish.children.bye.ooo;
                bye.visible = true;
                TweenMax.from(bye, 0.5, {alpha:0, y:bye.y + 200, ease:Cubic.easeOut, overwrite:1, delay:0.8});



                var face1 = spriteDatas.finish.children.pop.children.face1.ooo;
                TweenMax.to(face1, 0.5, {alpha:0, ease:Linear.easeOut, overwrite:1, delay:0.3});

                var face2 = spriteDatas.finish.children.pop.children.face2.ooo;
                face2.visible = true;
                TweenMax.from(face2, 0.5, {alpha:0, ease:Linear.easeOut, overwrite:1, delay:0.3});

                
                

                


            } else {
                alert('当时位置不能跳转到 car_leave');
            }
        break;



        case 'please_leave_soon':
            if (currentCommand == 'car_leave') {
                currentCommand = 'please_leave_soon';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------


                var bye = spriteDatas.finish.children.bye.ooo;
                TweenMax.to(bye, 0.5, {alpha:0, y:bye.y - 200, ease:Cubic.easeOut, overwrite:1});

                var lichang = spriteDatas.finish.children.lichang.ooo;
                lichang.visible = true;
                TweenMax.from(lichang, 0.5, {alpha:0, y:lichang.y + 200, ease:Cubic.easeOut, overwrite:1, delay:0.3});


                var face2 = spriteDatas.finish.children.pop.children.face2.ooo;
                TweenMax.to(face2, 0.5, {alpha:0, ease:Linear.easeOut, overwrite:1, delay:0.1});

                var face3 = spriteDatas.finish.children.pop.children.face3.ooo;
                face3.visible = true;
                TweenMax.from(face3, 0.5, {alpha:0, ease:Linear.easeOut, overwrite:1, delay:0.1});


                var pop = spriteDatas.finish.children.pop.ooo;
                tl1.clear();
                tl1.repeatDelay(0);
                tl1.yoyo(false);
                // tl1.to(pop, 2, {x:'-=50'});
                // tl1.to(pop, 0.2, {x:'-=50'});
                tl1.staggerTo([pop,face3], 0.1, {x:'+=10', delay:2});
                tl1.staggerTo([pop,face3], 0.1, {x:'-=20'});
                tl1.staggerTo([pop,face3], 0.1, {x:'+=20'});
                tl1.staggerTo([pop,face3], 0.1, {x:'-=10'});


            } else {
                alert('当时位置不能跳转到 please_leave_soon');
            }
        break;



        case 'customer_service':
            if (currentCommand == 'car_leave' || currentCommand == 'please_leave_soon') {
                

                if (currentCommand == 'car_leave') {

                    var bye = spriteDatas.finish.children.bye.ooo;
                    TweenMax.to(bye, 0.5, {alpha:0, y:bye.y - 200, ease:Cubic.easeOut, overwrite:1});

                    var face2 = spriteDatas.finish.children.pop.children.face2.ooo;
                    TweenMax.to(face2, 0.5, {alpha:0, ease:Linear.easeOut, overwrite:1, delay:0.1});

                } else if (currentCommand == 'please_leave_soon') {
                    
                    var lichang = spriteDatas.finish.children.lichang.ooo;
                    TweenMax.to(lichang, 0.5, {alpha:0, y:lichang.y - 200, ease:Cubic.easeOut, overwrite:1});

                    var face3 = spriteDatas.finish.children.pop.children.face3.ooo;
                    TweenMax.to(face3, 0.5, {alpha:0, ease:Linear.easeOut, overwrite:1, delay:0.1});
                }

                currentCommand = 'customer_service';
                currentCommandIndex = commands.indexOf(command);
                refBtnsText();
                // ----------
                

                var kefu = spriteDatas.finish.children.kefu.ooo;
                kefu.visible = true;
                TweenMax.from(kefu, 0.5, {alpha:0, y:kefu.y + 200, ease:Cubic.easeOut, overwrite:1, delay:0.3});

                var face4 = spriteDatas.finish.children.pop.children.face4.ooo;
                face4.visible = true;
                TweenMax.from(face4, 0.5, {alpha:0, ease:Linear.easeOut, overwrite:1, delay:0.1});

                var pop_body = spriteDatas.finish.children.pop.children.body.ooo;
                pop_body.texture = PIXI.loader.resources['assets/images/scene/textures/popBody_Gray.png'].texture;




                var pop = spriteDatas.finish.children.pop.ooo;
                tl1.clear();
                tl1.repeatDelay(0);
                tl1.yoyo(false);
                // tl1.to(pop, 2, {x:'-=50'});
                // tl1.to(pop, 0.2, {x:'-=50'});
                tl1.to(pop, 0.05, {x:'+=10', delay:2});
                tl1.to(pop, 0.05, {x:'-=10'});
                tl1.to(pop, 0.05, {x:'+=10'});
                tl1.to(pop, 0.05, {x:'-=10'});
                tl1.to(pop, 0.05, {x:'+=10'});
                tl1.to(pop, 0.05, {x:'-=10'});
                tl1.to(pop, 0.05, {x:'+=10'});
                tl1.to(pop, 0.05, {x:'-=10'});
                tl1.to(pop, 0.05, {x:'+=10'});
                tl1.to(pop, 0.05, {x:'-=10'});


            } else {
                alert('当时位置不能跳转到 customer_service');
            }
        break;

        

        case 'reload':
            location.reload();   
            break;

    }
}
// ---------- 可配置项 ----------


const socket = new WebSocket('ws://localhost:18750');

socket.addEventListener('open', function (event) {
    console.log('opening...')
    // socket.send('WebSocket Online')
})
const contactServer = () => {
        console.log('init ing ...')
        socket.send('Initialize');}

socket.addEventListener('message', function (event) {
    console.log('data recv...', event.data)
    go(event.data)
});


//默认配置
boi.defaultPage.templateId = 'scene';
boi.defaultPage.pageId = 'scene';
boi.defaultPage.constructor = intro_scene;//intro_scene
// boi.defaultPage.shiftMotionType = 'XIA_SHANG';


//本地测试配置
boi.defaultPageLocal.templateId = 'scene';//scene
boi.defaultPageLocal.pageId = 'scene';
boi.defaultPageLocal.constructor = intro_scene;//intro_scene



// boi.defaultFloatPage.templateId = 'video';
// boi.defaultFloatPage.pageId = 'video';

//页面内容宽高
boi.config.contentWidth = 1080;
boi.config.contentHeight = 2048;
//boi.config.resizeType = 'contain';
//boi.config.resizeType = 'width';






//附加的加载项
boi.preload.listAdd = [
    
];


//虚拟监测PV的项目根目录
// boi.monitor.pageRoot = '/tesla/newCarGuides/';


//站点地址
var sitePath = '';


//接口根地址
// var apiBaseUrl = '';


//分享设置

boi.shareInfo.default.title = 'title';
boi.shareInfo.default.desc = 'desc';
boi.shareInfo.default.imgUrl = sitePath + 'assets/images/sharePic.jpg';
boi.shareInfo.default.link = sitePath;

boi.shareInfo.timeline.title = 'title';





// url参数
var urlObj = null;

// 当前页面来源
// var siteSource;

//sessionid
// var sessionid;



//身份
// var identity;

//电话
// var tel = '4009100707';
var currentCommandIndex = 0;//无需修改
// var currentSubstepIndex = 0;//无需修改
var currentCommand = commands[currentCommandIndex];//上方数组





// ╔══════════════════     ═════════════════════╗

//浏览器宽高
var windowWidth = 1080;
var windowHeight = 2048;

//画布缩放比
var pixelRatio = 1;

// canvas内画面内容的宽高
const contentWidth = 1080 * pixelRatio;
const contentHeight = 2048 * pixelRatio;//37722

//渲染器的默认宽高
const rendererWidth = 1080 * pixelRatio;
var rendererHeight = 2048 * pixelRatio;

//浏览器与画布的比例(竖屏=宽度那一侧)
var bili_width_stage = $(window).width() / contentWidth;

// 显卡渲染类型
var renderType = "WebGL";
if (!PIXI.utils.isWebGLSupported()) {
    renderType = "canvas"
}
PIXI.utils.sayHello(renderType);


//渲染器
var renderer;

//舞台容器
var stage;


//纹理根路径
const texturesBasePath = 'assets/images/scene/textures/';

//纹理集合
var textures = {};

//纹理是否加载完成
var isLoadedTextures = false;

//总时间线
// var tm;

//循环时间线
// var tmC;

//画布的当前时间
var time_canvas = 0;

//body的当前时间，基于body分辨率
var time_body = 0;




//场景中的当前浏览的部分
// var currentPartIndex = 0;
// var currentPartName = '';
// var currentPartNames = ['特管家介绍','车辆使用','充电服务','服务保障','用车生活','尾页'];

//精灵数据
// var sprites = {};
var spriteDatas = {

    hi:{type:'container', x:0, y:0, children:{
        pop:{type:'container', x:-1420, y:395, children:{
            body:{type:'sprite', x:0, y:0, width:2685, height:2685, textures:'___ex', texture:'assets/images/scene/textures/popBody.png'},
            eyes:{type:'container', x:1755+10, y:671, children:{
                l:{type:'sprite', anchor:{x:0.5, y:0.5}, x:0+30, y:8+31, width:60, height:62, textures:'s1', texture:'eye_ping.png'},
                r:{type:'sprite', anchor:{x:0.5, y:0.5}, x:340+30, y:8+31, width:60, height:62, textures:'s1', texture:'eye_ping.png'},
                r2:{type:'sprite', x:329, y:0, width:81, height:79, textures:'s1', texture:'eyeR_zha.png', visible:false},
            }},
        }},
        bubble:{type:'container', x:631, y:182+0.7*257, alpha:0, pivot:{x:0*360, y:0.7*257}, scale:{x:0, y:0}, children:{
            frame:{type:'sprite', x:0, y:0, width:354, height:252, textures:'s1'},
            text:{type:'sprite', x:160, y:89, width:102, height:91, textures:'s1'},
        }},
    }},

    drive:{type:'container', x:0, y:0, children:{
        arrowsC:{type:'container', x:540, y:1024, pivot:{x:540, y:1024}, width:1080, height:2048, children:{
            arrows:{type:'container', x:0, y:0, children:{
                arrow1:{type:'sprite', x:286, y:0, textures:'s2', texture:'arrow_1.png'},
                arrow2:{type:'sprite', x:286, y:1500, textures:'s2', texture:'arrow_1.png'},
                arrow3:{type:'sprite', x:286, y:3000, textures:'s2', texture:'arrow_1.png'},
                // arrow3:{type:'sprite', x:286, y:0, textures:'s1'},
            }},
        }},
        stop:{type:'sprite', anchor:{x:0.5, y:0.5}, x:540, y:1024, textures:'s1', visible:false},
    }},

    tips:{type:'container', anchor:{x:0, y:1}, x:90, y:1966, children:{
        bubble:{type:'sprite', anchor:{x:0, y:1}, x:0, y:0, textures:'___ex', texture:'assets/images/scene/textures/tips_bubble.png'},
        text:{type:'text', x:260, y:-1196, text:text_tips, fontSize:92, fontWeight:'bold', fill:'#231f20', lineHeight:146, align:'center'},
    }},

    countDown:{type:'container', x:0, y:0, children:{
        n1:{type:'sprite', anchor:{x:0.5, y:0.5}, x:540, y:1024, textures:'s1'},
        n2:{type:'sprite', anchor:{x:0.5, y:0.5}, x:540, y:1024, textures:'s1'},
        n3:{type:'sprite', anchor:{x:0.5, y:0.5}, x:540, y:1024, textures:'s1'},
    }},

    wash:{type:'container', x:0, y:0, children:{
        bg:{type:'container', x:0, y:0, children:{

        }},
        cc:{type:'container', pivot:{x:212, y:212}, scale:{x:1, y:1}, width:424, height:424, x:540, y:480+360, children:{
            ccc:{type:'sprite', anchor:{x:0.5, y:0.5}, x:0+424/2, y:0+424/2, textures:'s1'},
            step:{type:'sprite', x:0, y:180, textures:'s1', texture:'step_1.png'},
            // step2:{type:'sprite', x:0, y:180, textures:'s1'},
            // step3:{type:'sprite', x:0, y:180, textures:'s1'},
            // step4:{type:'sprite', x:0, y:180, textures:'s1'},
            // step5:{type:'sprite', x:0, y:180, textures:'s1'},
            // step6:{type:'sprite', x:0, y:180, textures:'s1'},
        }},
        text:{type:'text', x:328, y:770+360, text:text_wash[0], fontSize:106, fontWeight:'bold', fill:'#e0fe2c', lineHeight:150, align:'center', wordWrapWidth:424},
    }},

    finish:{type:'container', x:0, y:0, children:{
        text:{type:'text', x:270, y:770+360, text:text_finish, fontSize:90, fontWeight:'bold', fill:'#e0fe2c', lineHeight:130, align:'center', wordWrapWidth:540},
        ccc:{type:'sprite', anchor:{x:0.5, y:0.5}, x:540, y:480+360, width:424, height:424, textures:'s1'},
        
        bye:{type:'sprite', x:202, y:198, textures:'s1', visible:false},
        lichang:{type:'sprite', x:135, y:210, textures:'s1', visible:false},
        kefu:{type:'sprite', x:135, y:210, textures:'s1', visible:false},
        longcar:{type:'text', x:135, y:210, text:'车长超出清洗范围\n请离场', fontSize:80, lineHeight:116, fontWeight:'bold', fill:'#fff', wordWrapWidth:2000, visible:false},

        pop:{type:'container', pivot:{x:332/2, y:332/2}, x:540, y:480+360, scale:{x:1, y:1}, children:{

            body:{type:'sprite', x:0, y:0, width:332, height:332, textures:'___ex', texture:'assets/images/scene/textures/popBody.png'},
            // bodyGray:{type:'sprite', x:0, y:0, width:332, height:332, textures:'___ex', texture:'assets/images/scene/textures/popBody_Gray.png'},

            face1:{type:'container', x:73+50, y:82, children:{
                eyeL:{type:'sprite', anchor:{x:0.5, y:0.5}, x:4+9.5, y:10+9, width:19, height:18, textures:'s1', texture:'eyeL_zha.png'},
                eyeR:{type:'sprite', anchor:{x:0.5, y:0.5}, x:56+9.3, y:10+9, width:18.6, height:18, textures:'s1', texture:'eyeR_zha.png'},
                mouth:{type:'sprite', x:2, y:43, width:76, height:27, textures:'s1', texture:'mouth_xiao.png'},
            }},

            face2:{type:'container', x:135, y:32, visible:false, children:{
                eyeL:{type:'sprite', anchor:{x:0.5, y:0.5}, x:19+4.25, y:17+4.4, width:8.5, height:8.8, textures:'s1', texture:'eye_ping.png'},
                eyeR:{type:'sprite', anchor:{x:0.5, y:0.5}, x:53+4.25, y:17+4.4, width:8.5, height:8.8, textures:'s1', texture:'eye_ping.png'},
                mouth:{type:'sprite', x:2, y:40, width:76, height:27, textures:'s1', texture:'mouth_xiao.png'},
            }},

            face3:{type:'container', x:150, y:88, visible:false, children:{
                eyeL:{type:'sprite', x:5, y:6, width:19, height:18, textures:'s1', texture:'eyeL_zha.png'},
                eyeR:{type:'sprite', x:57, y:6, width:18.6, height:18, textures:'s1', texture:'eyeR_zha.png'},
                mouth:{type:'sprite', x:22, y:54, width:47, height:20, textures:'s1', texture:'mouth_ku.png'},
            }},

            face4:{type:'container', x:142, y:72, visible:false, children:{
                eyeL:{type:'sprite', x:0, y:11, width:22, height:20, textures:'s1', texture:'eyeL_x.png'},
                eyeR:{type:'sprite', x:57, y:7, width:23, height:22, textures:'s1', texture:'eyeR_x.png'},
                mouth:{type:'sprite', x:22, y:57, width:45, height:15, textures:'s1', texture:'mouth_dou.png'},
            }},
        }},
    }},

    /* guanjia:{type:'container', x:0, y:0, height:3873, children:{
        title:{type:'sprite', x:245, y:92},
        tel:{type:'container', x:51, y:294, children:{
            bg:{type:'sprite', x:0, y:0, width:1068, height:1332, textures:'box1'},
            title:{type:'sprite', x:360, y:123},
            subtitle:{type:'sprite', x:211, y:222},
            // pic:{type:'sprite', x:192, y:318, textures:'pic'},
            pic:{type:'container', x:192, y:318, children:{
                ren:{type:'sprite', x:146, y:301, textures:'pic'},
                qipao1:{type:'sprite', x:0, y:243, textures:'pic'},
                qipao2:{type:'sprite', x:203, y:0, textures:'pic'}
            }},
            btn:{type:'sprite', x:294+240, y:1110+54, anchor:{x:0.5, y:0.5}, ani:[{name:'bobo'}]}
        }},
       
        qicheng:{type:'container', x:525, y:3389, children:{
            label:{type:'sprite', x:7, y:0},
            arrow:{type:'sprite', x:0, y:64}
        }},
        kk:{type:'container', x:357, y:3633, children:{
            lu:{type:'sprite', x:198, y:0, textures:'road', texture:'guanjia_lu1.png'}
        }}
        
    }}, */

    

}

// var stationArray = [spriteDatas.s2, spriteDatas.s1, spriteDatas.s3, spriteDatas.s4];
// var stationNameArray = currentPartNames.slice(1,5);
// console.log(stationNameArray);


// ╚════════════════════════════════════════════════════╝

//页面未显示前执行的初始函数
/*boi.config.onInit = function (onComplete) {
    
    if (typeof onComplete == "function") {onComplete()};
    
}*/



// 项目初始化
boi.config.onInit = function () {
    
}


boi.config.onLoaded = function (onComplete) {
    preloadTextures();
    function preloadTextures() {
        // console.log('sss');

        //预加载
        var resources = [
            'assets/images/scene/textures/s1.json',
            'assets/images/scene/textures/s2.json',
            'assets/images/scene/textures/popBody.png',
            'assets/images/scene/textures/popBody_Gray.png',
            'assets/images/scene/textures/tips_bubble.png'
        ];


        PIXI.loader.add(resources).on("progress", function (target, resource) {
            // console.log('pixi加载进度：' + target.progress + '%');
        }).load(onLoaded);


        function onLoaded() {

            // console.log('onLoaded');
            textures.s1 = PIXI.loader.resources["assets/images/scene/textures/s1.json"].textures;
            textures.s2 = PIXI.loader.resources["assets/images/scene/textures/s2.json"].textures;

            isLoadedTextures = true;

            onComplete();
        }
    }

    
}






//loading进度处理
boi.loading.onProgress = function(_progress) {
    $('#loading_progress span').text((_progress*100|0));
}





function refBtnsText(){

    $('#scene #btn1').hide();
    $('#scene #btn2').hide();
    $('#scene #btn3').hide();
    $('#scene #titleOther').hide();

    if (currentCommand == 'arrows_change3') {
        //停止
        $('#scene #btnNext').text('stop_driving');
        //回退
        $('#scene #btn1').show();
        $('#scene #btn1').text('car_back');
        //车过长
        $('#scene #btn2').show();
        $('#scene #btn2').text('long_car');

        $('#scene #titleOther').show();

    } else if (currentCommand == 'car_back') {
        //停止
        $('#scene #btnNext').text('stop_driving');
        //前进3
        $('#scene #btn1').show();
        $('#scene #btn1').text('arrows_change3');

        $('#scene #titleOther').show();

    } else if (currentCommand == 'stop_driving' || currentCommand == 'risk_warning' || currentCommand == 'countdown') {
        //下一步
        $('#scene #btnNext').text(commands[currentCommandIndex+1]);
        //前进3
        $('#scene #btn1').text('arrows_change3');
        $('#scene #btn1').show();
        //回退
        $('#scene #btn2').text('car_back');
        $('#scene #btn2').show();

        $('#scene #titleOther').show();

    } else if (currentCommand == 'long_car') {
        //重新加载
        $('#scene #btnNext').text('reload');

    } else if (currentCommand == 'car_leave') {
        //重新加载
        $('#scene #btnNext').text('reload');
        //尽快离场
        $('#scene #btn1').text('please_leave_soon');
        $('#scene #btn1').show();
        //呼叫客服
        $('#scene #btn2').text('customer_service');
        $('#scene #btn2').show();

    } else if (currentCommand == 'please_leave_soon') {
        //重新加载
        $('#scene #btnNext').text('reload');
        //尽快离场
        $('#scene #btn1').text('customer_service');
        $('#scene #btn1').show();

    } else {
        $('#scene #btnNext').text(commands[currentCommandIndex+1]);
    }

    


}





// ╔══════════════════ scene 场景页 ═════════════════════╗
function intro_scene() {


   
    $('#scene #btnNext').click(btnHandler);
    $('#scene #btn1').click(btnHandler);
    $('#scene #btn2').click(btnHandler);
    $('#scene #btn3').click(btnHandler);

    function btnHandler(e) {
        var command = e.currentTarget.textContent;
        go(command);
    }

    




    




    // ------ pixi ------ ------------------------------------------------------------------------
    
    // tm = new TimelineMax({ paused: true });
    // tmC = new TimelineMax();

    
    // 渲染器
    renderer = PIXI.autoDetectRenderer(rendererWidth, rendererHeight, {
        antialias: true,
        // resolution: 2,
        transparent: true
    });

    //将舞台添加到，页面中
    $('#scene #baseScene').append(renderer.view);

    //创建元素容器，类似 ‘组’概练，Container可以嵌套Container
    stage = new PIXI.Container();

    //是否可点击，修正点击误触
    // var tapEnabled = true;



    //装载
    setupScenePage();
    // console.log(sprites);


    setTimeout(start, 100);

    


    function start() {
        
        // 拖拽处理
        // touchHandler();


        //设置动画参数
        // resetAnimate();

        //开始渲染
        render();

        //第一次seek
        // seekHandler();

        // 画面旋转设置
        onWindowResize();
        $(window).resize(onWindowResize);



        go('screen_saver');

    }

    

    //持续渲染场景 以每秒60fps渲染 --------------------------
    function render() {
        // console.log('render');
        //渲染
        renderer.render(stage);

        //手机兼容性处理
        requestAnimationFrame(render);
                
    }

    

/*     //跳至动画位置
    function seekHandler() {
        // //匹配导航
        // matchMenu();

        //匹配显示
        // refScenePartShow();

        //范围检测
        range();
        
        //动画
        tm.seek(time_canvas);
    } */




    //装载场景
    function setupScenePage() {
        
        
        //创建容器和精灵
        for (var i in spriteDatas) {
            var sd_i = spriteDatas[i];
            if (sd_i.type == 'container') {


                //容器
                // stage.addChild(newContainer(sd_i));
                var ooo = newContainer(sd_i);
                if (i == 'hi') {
                    spriteDatas[i].isAddShow = true;
                    stage.addChild(ooo);
                }
                // sprites.i = ooo;
                // rootContainer.push(ooo);

                for (var j in sd_i.children) {
                    var sd_i_j = sd_i.children[j];
                    // console.log(sd_i_j.type);
                    if (sd_i_j.type == 'container') {


                        //容器
                        sd_i.ooo.addChild(newContainer(sd_i_j));
                        // sprites.i.j = ooo;
                        if (sd_i_j.ani) applyMotion(sd_i_j);


                        for (var m in sd_i_j.children) {
                            var sd_i_j_m = sd_i_j.children[m];
                            if (sd_i_j_m.type == 'container') {


                                //容器
                                sd_i_j.ooo.addChild(newContainer(sd_i_j_m));
                                // sprites.i.j.m = ooo;
                                if (sd_i_j_m.ani) applyMotion(sd_i_j_m);


                                for (var n in sd_i_j_m.children) {
                                    var sd_i_j_m_n = sd_i_j_m.children[n];
                                    if (sd_i_j_m_n.type == 'container') {


                                        //容器
                                        sd_i_j_m.ooo.addChild(newContainer(sd_i_j_m_n));
                                        // sprites.i.j.m.n = ooo;
                                        if (sd_i_j_m_n.ani) applyMotion(sd_i_j_m_n);


                                        for (var v in sd_i_j_m_n.children) {
                                            var sd_i_j_m_n_v = sd_i_j_m_n.children[v];
                                            if (sd_i_j_m_n_v.type == 'sprite') {


                                                //sprite
                                                sd_i_j_m_n.ooo.addChild(newSprite(getTexture(sd_i_j_m_n_v, i, i + '_' + j + '_' + m + '_' + n + '_' + v + '.png'), sd_i_j_m_n_v));
                                                // sprites.i.j.m.n.v = ooo;
                                                if (sd_i_j_m_n_v.ani) applyMotion(sd_i_j_m_n_v);
                                            } else if (sd_i_j_m_n_v.type == 'text') {

                                                //text
                                                sd_i_j_m_n.ooo.addChild(newText(sd_i_j_m_n_v));
                                                // sprites.i.j.m.n.v = ooo;
                                                if (sd_i_j_m_n_v.ani) applyMotion(sd_i_j_m_n_v);
                                            }
                                        }

                                    } else if (sd_i_j_m_n.type == 'sprite') {
                                        


                                        //sprite
                                        sd_i_j_m.ooo.addChild(newSprite(getTexture(sd_i_j_m_n, i, i + '_' + j + '_' + m + '_' + n + '.png'), sd_i_j_m_n));
                                        // sprites.i.j.m.n = ooo;
                                        if (sd_i_j_m_n.ani) applyMotion(sd_i_j_m_n);
                                    } else if (sd_i_j_m_n.type == 'text') {

                                        //text
                                        sd_i_j_m.ooo.addChild(newText(sd_i_j_m_n));
                                        // sprites.i.j.m.n = ooo;
                                        if (sd_i_j_m_n.ani) applyMotion(sd_i_j_m_n);
                                    }
                                }


                            } else if (sd_i_j_m.type == 'sprite') {


                                //sprite
                                sd_i_j.ooo.addChild(newSprite(getTexture(sd_i_j_m, i, i + '_' + j + '_' + m + '.png'), sd_i_j_m));
                                // sprites.i.j.m = ooo;
                                if (sd_i_j_m.ani) applyMotion(sd_i_j_m);
                            } else if (sd_i_j_m.type == 'text') {

                                //text
                                sd_i_j.ooo.addChild(newText(sd_i_j_m));
                                // sprites.i.j.m = ooo;
                                if (sd_i_j_m.ani) applyMotion(sd_i_j_m);
                            }
                        }


                    } else if (sd_i_j.type == 'sprite') {


                        //sprite
                        sd_i.ooo.addChild(newSprite(getTexture(sd_i_j, i, i + '_' + j + '.png'), sd_i_j));
                        // sprites.i.j = ooo;
                        if (sd_i_j.ani) applyMotion(sd_i_j);
                    } else if (sd_i_j.type == 'text') {

                        //text
                        sd_i.ooo.addChild(newText(sd_i_j));
                        // sprites.i.j = ooo;
                        if (sd_i_j.ani) applyMotion(sd_i_j);
                    }
                }
                


            } else if (spriteDatas[i].type == 'sprite' || spriteDatas[i].type == 'text') {


                //sprite
                console.log('不存在这种情况');
            }








            
        }



        function getTexture(spriteData, defaultTexturesField, defaultTexture) {
            // console.log(spriteData);
            if (spriteData.textures == '___ex' && spriteData.texture) {//不使用纹理集,直接使用定义的纹理
                // console.log(spriteData.texture);
                texture = PIXI.loader.resources[spriteData.texture].texture;
            } else if (spriteData.textures && spriteData.texture) {//定义了纹理集合纹理，使用定义的纹理集和纹理
                texture = textures[spriteData.textures][spriteData.texture];
            } else if (spriteData.textures) {//只定义了纹理集，名称匹配纹理
                texture = textures[spriteData.textures][defaultTexture];
            } else {//均无定义，名称匹配纹理集和纹理
                texture = textures[defaultTexturesField][defaultTexture];
            }
            return texture;
        }

        


        function newSprite(texture, spriteData) {
            
            var ooo = new PIXI.Sprite(texture);
            ooo.x = spriteData.x;
            ooo.y = spriteData.y;
            if (spriteData.width) ooo.width = spriteData.width;
            if (spriteData.height) ooo.height = spriteData.height;
            if (spriteData.scale) ooo.scale.set(spriteData.scale.x, spriteData.scale.y);
            if (spriteData.anchor) ooo.anchor.set(spriteData.anchor.x, spriteData.anchor.y);
            if (spriteData.alpha || spriteData.alpha==0) ooo.alpha = spriteData.alpha;
            if (spriteData.visible == false) ooo.visible = false;
            spriteData.ooo = ooo;
            // container.addChild(ooo);
            
            //加动画
            // if (spriteData.ani) applyMotion(spriteData);
      
            return ooo;
            
        }

        function newText(spriteData) {
            let style = new PIXI.TextStyle({
                fontFamily: 'Arial', // 字体
                fontSize: spriteData.fontSize ? spriteData.fontSize : 32, // 字号大小
                fontStyle: spriteData.fontStyle ? spriteData.fontStyle : 'normal', // 斜体
                fontWeight: spriteData.fontWeight ? spriteData.fontWeight : 'normal', //粗体
                fill: spriteData.fill ? spriteData.fill : '#ffffff', // 填充颜色
                wordWrap: spriteData.wordWrap ? spriteData.wordWrap : true, // 是否换行
                wordWrapWidth: spriteData.wordWrapWidth ? spriteData.wordWrapWidth : 440, // 每行的长度
                lineHeight: spriteData.lineHeight,
                align: spriteData.align ? spriteData.align : 'left',
              });
               
              let ooo = new PIXI.Text(spriteData.text, style);
              ooo.x = spriteData.x;
              ooo.y = spriteData.y;
            //   if (spriteData.width) {ooo.width = spriteData.width} else {ooo.width = 440};
                // if (spriteData.height) ooo.height = spriteData.height;
              if (spriteData.scale) ooo.scale.set(spriteData.scale.x, spriteData.scale.y);
                if (spriteData.anchor) ooo.anchor.set(spriteData.anchor.x, spriteData.anchor.y);
                if (spriteData.alpha || spriteData.alpha==0) ooo.alpha = spriteData.alpha;
                if (spriteData.visible == false) ooo.visible = false;
              spriteData.ooo = ooo;
               
              return ooo;
            /* let style = new PIXI.TextStyle({
                fontFamily: 'Arial', // 字体
                fontSize: 36, // 字号大小
                fontStyle: 'italic', // 斜体
                fontWeight: 'bold', //粗体
                fill: ['#ffffff', '#00ff99'], // 填充颜色
                stroke: '#4a1850', // 描边颜色
                strokeThickness: 5, // 描边宽度
                dropShadow: true, // 阴影
                dropShadowColor: '#000000', // 阴影颜色
                dropShadowBlur: 4, // 阴影模糊半径
                dropShadowAngle: Math.PI / 6, // 阴影投射方向
                dropShadowDistance: 6, // 阴影投射距离
                wordWrap: true, // 是否换行
                wordWrapWidth: 440, // 每行的长度
              });
               
              let richText = new PIXI.Text('This is richText , \n样式文本 , \nneed set style', style);
              richText.x = 50;
              richText.y = 250;
               
              stage.addChild(richText); */
        }


        function newContainer(spriteData){
            var ooo = new PIXI.Container();
            ooo.x = spriteData.x;
            ooo.y = spriteData.y;
            if (spriteData.width) ooo.width = spriteData.width;
            if (spriteData.height) ooo.height = spriteData.height;
            if (spriteData.scale) ooo.scale.set(spriteData.scale.x, spriteData.scale.y);
            // if (spriteData.anchor) ooo.anchor.set(spriteData.anchor.x, spriteData.anchor.y);
            if (spriteData.pivot) {ooo.pivot.x = spriteData.pivot.x;ooo.pivot.y = spriteData.pivot.y;}
            if (spriteData.alpha || spriteData.alpha==0) ooo.alpha = spriteData.alpha;
            if (spriteData.visible == false) ooo.visible = false;
            spriteData.ooo = ooo;
            // container.addChild(ooo);

            //加动画
            // if (spriteData.ani) applyMotion(spriteData);

            return ooo;
        }





        //额外加的动画
       /*  addMotion();
        function addMotion() {
            
            




        } */







        function applyMotion(spriteData){

            // return;

            //默认来一个渐显
            // console.log(getPositionY(spriteData));
            // tm.from(spriteData.ooo, 1000, { alpha: 0, y:spriteData.y + 100}, getPositionY(spriteData)-rendererHeight-200);

            var anis = {
                rightBobo:function (spriteData, aniData){
                    tmC.to(spriteData.ooo, 0.5, {x:spriteData.x+8, ease:Linear.easeOut, repeat:-1, yoyo:true}, 0+aniData.delay);
                },
                bobo:function (spriteData, aniData) {
                    tmC.to(spriteData.ooo.scale, 1, {x:1.05, y:1.05, ease:Linear.easeOut, repeat:-1, yoyo:true}, 2);
                },
                moveIn:function (spriteData, aniData) {
                    tm.from(spriteData.ooo, aniData.duration ? aniData.duration : 1500, { x: spriteData.x + aniData.x, y: spriteData.y + aniData.y, alpha:0}, getPositionY(spriteData)-rendererHeight+aniData.delay);
                },
                peng:function (spriteData, aniData) {
                    tm.from(spriteData.ooo, aniData.duration ? aniData.duration : 1000, { alpha:0}, getPositionY(spriteData)-rendererHeight+aniData.delay);
                    tm.from(spriteData.ooo.scale, aniData.duration ? aniData.duration : 1000, { x:0, y:0, ease:Back.easeOut}, getPositionY(spriteData)-rendererHeight+aniData.delay);
                },
                zhang:function (spriteData, aniData) {
                    // console.log('zhang');
                    tm.from(spriteData.ooo, aniData.duration ? aniData.duration : 1200, { alpha:0}, getPositionY(spriteData)-rendererHeight+aniData.delay);
                    tm.from(spriteData.ooo.scale, aniData.duration ? aniData.duration : 1200, { x:aniData.x, y:aniData.y, ease:Power3.easeOut}, getPositionY(spriteData)-rendererHeight+aniData.delay);
                },
                show:function (spriteData, aniData) {
                    tm.from(spriteData.ooo, aniData.duration ? aniData.duration : 1200, { alpha: 0}, getPositionY(spriteData)-rendererHeight+aniData.delay);
                },
                speed:function (spriteData, aniData){
                    tm.fromTo(spriteData.ooo, rendererHeight, { y: spriteData.y + aniData.quantity/2}, { y: spriteData.y - aniData.quantity/2}, getPositionY(spriteData)-rendererHeight+aniData.delay);
                }
            }
            

            //执行指定的动画
            if (spriteData.ani) {
                for (var i in spriteData.ani) {
                    // eval(spriteData.ani[i].name + '(spriteData, spriteData.ani[i])');

                    // console.log(spriteData.ani[i].name);
                    // console.log(anis[spriteData.ani[i].name]);
                    anis[spriteData.ani[i].name](spriteData, spriteData.ani[i]);
                }
            }
            
  
            

        }

        function getPositionY(spriteData) {
            var y = spriteData.y;
            
            if (spriteData.ooo.parent) {
                y += spriteData.ooo.parent.y;
                if (spriteData.ooo.parent.parent) {
                    y += spriteData.ooo.parent.parent.y;
                    if (spriteData.ooo.parent.parent.parent) {
                        y += spriteData.ooo.parent.parent.parent.y;
                        if (spriteData.ooo.parent.parent.parent.parent) {
                            y += spriteData.ooo.parent.parent.parent.parent.y;
                            if (spriteData.ooo.parent.parent.parent.parent.parent) {
                                y += spriteData.ooo.parent.parent.parent.parent.parent.y;
                            }
                        }
                    }
                }
            }

            return y;
            
        }


        //////////////添加事件-----------------



     






        
        


    }








    //重置动画
/*     function resetAnimate() {
        //设置动画
    
        //总时长
        var allDuration = contentHeight - rendererHeight;
    
        //修正seek
        if (time_canvas > allDuration) time_canvas = allDuration;
    
        //主场景位移
        tm.fromTo(stage, allDuration, { y: 0, ease: Linear.easeOut, overwrite: 1 }, { y: -allDuration, ease: Linear.easeOut, overwrite: 1 }, 0);
        // tm.fromTo('#scene #exLevel_main', allDuration, { y: 0, ease: Linear.easeOut, overwrite: 1 }, { y: -allDuration/pixelRatio, ease: Linear.easeOut, overwrite: 1 }, 0);
    } */




    /* function startMotion() {

    } */




    

    function onWindowResize() {
        //获取真实浏览器宽高
        windowWidth = $(window).width();
        windowHeight = $(window).height();

        bili_width_stage = windowWidth / contentWidth;
        rendererHeight = windowHeight / bili_width_stage;
        if (renderer) renderer.resize(rendererWidth, rendererHeight);

        //缩放exLevel
        $('#scene #exLevel').css('transform', 'scale(' + bili_width_stage*pixelRatio + ')');
        // $('#scene #exLevel').scale(bili_width_stage*3);
    }




    
   
}
// ╚════════════════════════════════════════════════════╝







/* //进入开始
function intro_hi() {

}

//切换到前进动画
function shiftTo_drive() {

}

//切换到提示
function shiftTo_tips() {

}

//切换到倒计时
function shiftTo_countDown() {

}

//切换到清洗
function shiftTo_wash() {

}

//切换到完成
function shiftTo_finish() {
    
}

//回到开始
function re_hi() {

} */












//<!------------------------------ 其他部分 ------------------------------ -->


//动画效果 - 呼吸
function motion_bo(obj) {
    // console.log(obj);
    
    TweenMax.to(obj, 0.3, {scale:0.92, ease:Cubic.easeOut, overwrite:1, onComplete:onC1});
    function onC1() {
        TweenMax.to(obj, 0.3, {scale:1.03, ease:Cubic.easeOutIn, overwrite:1, onComplete:onC2});
    }
    function onC2() {
        TweenMax.to(obj, 0.3, {scale:0.98, ease:Cubic.easeOutIn, overwrite:1, onComplete:onC3});
    }
    function onC3() {
        TweenMax.to(obj, 0.3, {scale:1, ease:Cubic.easeOutIn, overwrite:1});
    }
}
