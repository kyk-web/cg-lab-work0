# src/Work0/physics.py
#放粒子物理更新
import taichi as ti#用taichi框架做并行计算+渲染
from .config import *#把config里面的常量全拿来用

# 1. 数据结构定义：在显存中开辟空间
pos = ti.Vector.field(2, dtype=float, shape=NUM_PARTICLES)#位置
vel = ti.Vector.field(2, dtype=float, shape=NUM_PARTICLES)#速度

@ti.kernel#是taichi的kernel，会被编译，然后在cpuorgpu后端执行
def init_particles():
    """初始化每一个粒子的随机坐标"""
    for i in range(NUM_PARTICLES):
        pos[i] = [ti.random(), ti.random()]
        vel[i] = [0.0, 0.0]

@ti.kernel
def update_particles(mouse_x: float, mouse_y: float):
    """物理更新：由 GPU 并行执行"""
    for i in range(NUM_PARTICLES):
        # 计算方向与距离
        mouse_pos = ti.Vector([mouse_x, mouse_y])#把穿进去的鼠标坐标变成2D向量
        dir = mouse_pos - pos[i]#从粒子指向鼠标的向量
        dist = dir.norm()#dir的长度，即粒子到鼠标的距离
        
        # 施加引力与阻力
        if dist > 0.05:
            vel[i] += dir.normalized() * GRAVITY_STRENGTH#粒子速度朝鼠标方向增加一点，让它追着鼠标跑
            
        vel[i] *= DRAG_COEF # 空气阻力，速度衰减
        pos[i] += vel[i]#新位置=旧位置+速度

        # 边框碰撞检测
        for j in ti.static(range(2)):
            if pos[i][j] < 0:
                pos[i][j] = 0.0
                vel[i][j] *= BOUNCE_COEF#反弹，速度反向并衰减
            elif pos[i][j] > 1:
                pos[i][j] = 1.0
                vel[i][j] *= BOUNCE_COEF#反弹，速度反向并衰减