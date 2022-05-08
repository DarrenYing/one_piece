import taichi as ti
from taichi.math import *

from scene import Scene

scene = Scene(voxel_edges=0, exposure=2)
scene.set_directional_light((0.5, 0.5, 0.8), 0.5, (1, 0.8, 0.6))
scene.set_background_color(vec3(0.204, 0.596, 0.859))


@ti.func
def draw_circle(center, radius, height, color):
    for x, y, z in ti.ndrange((-radius, radius), (0, height), (-radius, radius)):
        d = vec2(x, z).norm()
        if d <= radius:
            scene.set_voxel(center + vec3(x, y, z), 1, color)


@ti.func
def draw_box(loc0, len_x, len_y, len_z, color):
    for i, j, k, in ti.ndrange((loc0.x, loc0.x + len_x), (loc0.y, loc0.y + len_y), (loc0.z, loc0.z + len_z)):
        scene.set_voxel(ivec3(i, j, k), 1, color)


@ti.kernel
def initialize_voxels():
    # 路飞
    base_pos = vec3(0, 40, 0)
    draw_circle(base_pos, radius=8, height=3, color=vec3(1, 1, 0))  # 帽子
    draw_box(base_pos + vec3(-5, 3, -5), 10, 3, 10, color=vec3(1, 0, 0))
    draw_box(base_pos + vec3(-5, 6, -5), 10, 3, 10, color=vec3(1, 1, 0))
    draw_box(base_pos + vec3(-5, -8, -3), 10, 8, 8, color=vec3(1, 0.92, 0.65))  # 头
    draw_box(base_pos + vec3(-5, -8, -5), 10, 8, 2, color=vec3(0, 0, 0))
    draw_box(base_pos + vec3(-2, -11, -2), 4, 3, 4, vec3(1, 1, 1))  # 脖子
    draw_box(vec3(-2, 17, -4), 4, 12, 8, vec3(1, 1, 1))  # 身体
    draw_box(vec3(-5, 17, -5), 3, 13, 10, vec3(1, 0, 0))
    draw_box(vec3(2, 17, -5), 3, 13, 10, vec3(1, 0, 0))
    draw_box(vec3(-8, 23, -4), 3, 6, 8, vec3(1, 0, 0))  # 手臂
    draw_box(vec3(5, 23, -4), 3, 6, 8, vec3(1, 0, 0))
    draw_box(vec3(-11, 19, -3), 3, 7, 6, vec3(1, 0, 0))
    draw_box(vec3(8, 19, -3), 3, 7, 6, vec3(1, 0, 0))
    draw_box(vec3(-11, 17, -2), 3, 2, 4, vec3(1, 1, 1))
    draw_box(vec3(8, 17, -2), 3, 2, 4, vec3(1, 1, 1))
    draw_box(vec3(-6, 14, -4), 12, 3, 8, vec3(1, 1, 0))  # 腰带
    draw_box(vec3(2, 11, 4), 4, 3, 2, vec3(1, 1, 0))
    draw_box(vec3(-5, 11, -4), 10, 3, 8, vec3(0.1, 0.1, 0.8))  # 裤子
    draw_box(vec3(-5, 8, -2), 3, 3, 4, vec3(0.1, 0.1, 0.8))  # 左
    draw_box(vec3(-5, 2, -2), 3, 6, 4, vec3(1, 1, 1))
    draw_box(vec3(2, 8, -2), 3, 3, 4, vec3(0.1, 0.1, 0.8))  # 右
    draw_box(vec3(2, 2, -2), 3, 6, 4, vec3(1, 1, 1))
    draw_box(vec3(-5, 0, -2), 3, 2, 5, vec3(0.6, 0.2, 0.2))  # 鞋子
    draw_box(vec3(2, 0, -2), 3, 2, 5, vec3(0.6, 0.2, 0.2))
    # 索隆
    draw_box(vec3(-29, 37, -4), 8, 9, 8, vec3(1, 0.92, 0.65))  # 头
    draw_box(vec3(-29, 46, -4), 8, 3, 8, vec3(0, 1, 0))
    draw_box(vec3(-27, 34, -2), 4, 3, 4, vec3(1, 1, 1))  # 脖子
    draw_box(vec3(-27, 27, -4), 4, 7, 8, vec3(1, 1, 1))  # 身体
    draw_box(vec3(-27, 20, -4), 4, 7, 8, vec3(0.1, 0.8, 0.1))
    draw_box(vec3(-30, 20, -4), 3, 14, 8, vec3(0, 0.2, 0))
    draw_box(vec3(-23, 20, -4), 3, 14, 8, vec3(0, 0.2, 0))
    draw_box(vec3(-33, 29, -2), 3, 5, 4, vec3(0, 0.2, 0))  # 手臂
    draw_box(vec3(-20, 29, -2), 3, 5, 4, vec3(0, 0.2, 0))
    draw_box(vec3(-36, 18, -2), 3, 13, 4, vec3(0, 0.2, 0))
    draw_box(vec3(-17, 18, -2), 3, 13, 4, vec3(0, 0.2, 0))
    draw_box(vec3(-17, 25, -2), 3, 4, 4, vec3(0.2, 0, 0))
    draw_box(vec3(-36, 16, -2), 3, 2, 4, vec3(1, 1, 1))
    draw_box(vec3(-17, 16, -2), 3, 2, 4, vec3(1, 1, 1))
    draw_box(vec3(-30, 17, -4), 10, 3, 8, vec3(0.3, 0, 0))  # 腰带
    draw_box(vec3(-33, 17, -9), 3, 3, 18, vec3(0.8, 0.1, 0.1))  # 刀鞘
    draw_box(vec3(-20, 8, -2), 3, 10, 4, vec3(0.3, 0, 0))
    draw_box(vec3(-30, 3, -4), 10, 14, 8, vec3(0, 0.2, 0))  # 裤子
    draw_box(vec3(-30, 0, -3), 3, 3, 6, vec3(0, 0, 0))  # 鞋子
    draw_box(vec3(-23, 0, -3), 3, 3, 6, vec3(0, 0, 0))
    # 山治
    draw_box(vec3(21, 38, -4), 8, 8, 8, vec3(1, 0.92, 0.65))  # 头
    draw_box(vec3(21, 44, -4), 8, 5, 8, vec3(1, 1, 0))  # 头发
    draw_box(vec3(26, 44, -3), 3, 3, 7, vec3(1, 0.92, 0.65))
    draw_box(vec3(21, 41, 1), 2, 3, 3, vec3(1, 1, 0))
    draw_box(vec3(21, 38, -4), 8, 6, 3, vec3(1, 1, 0))
    draw_box(vec3(23, 32, -2), 4, 6, 4, vec3(1, 1, 1))  # 脖子
    draw_box(vec3(20, 32, -4), 3, 3, 8, vec3(1, 1, 0))  # 领带
    draw_box(vec3(27, 32, -4), 3, 3, 8, vec3(1, 1, 0))
    draw_box(vec3(20, 20, -4), 9, 12, 7, vec3(0, 0, 0))  # 身体
    draw_box(vec3(23, 29, -4), 4, 3, 8, vec3(1, 1, 1))
    draw_box(vec3(17, 29, -3), 3, 6, 6, vec3(0, 0, 0))  # 手臂
    draw_box(vec3(29, 29, -3), 3, 6, 6, vec3(0, 0, 0))
    draw_box(vec3(14, 23, -3), 3, 9, 6, vec3(0, 0, 0))
    draw_box(vec3(14, 20, -3), 3, 3, 6, vec3(1, 1, 1))
    draw_box(vec3(32, 25, -3), 3, 7, 6, vec3(0, 0, 0))
    draw_box(vec3(32, 25, 3), 3, 3, 5, vec3(0, 0, 0))
    draw_box(vec3(32, 25, 8), 3, 3, 3, vec3(1, 1, 1))
    draw_box(vec3(20, 0, -3), 3, 20, 6, vec3(0.01, 0.01, 0.01))  # 腿
    draw_box(vec3(26, 0, -3), 3, 20, 6, vec3(0.01, 0.01, 0.01))
    draw_box(vec3(20, 0, 3), 3, 3, 2, vec3(0.02, 0.02, 0.02))  # 鞋子
    draw_box(vec3(26, 0, 3), 3, 3, 2, vec3(0.03, 0.03, 0.03))


initialize_voxels()
scene.finish()
