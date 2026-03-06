# cg-lab-work0：基于Taichi的GPU粒子群交互仿真

## 一、项目简介

本项目基于Python与Taichi实现了一个面向图形计算入门的GPU粒子群交互仿真系统。项目采用 `src` 目录结构组织代码，通过模块化方式划分参数配置、物理计算与渲染显示三部分，并借助Taichi的GPU后端完成大量粒子的并行更新与实时可视化。

程序运行后会创建交互式窗口，窗口中的粒子在鼠标位置作用下产生明显的聚集与跟随行为；当粒子运动到窗口边界时，会发生碰撞与反弹，从而形成连续、流畅的动态粒子效果。该项目体现了GPU并行计算在粒子系统仿真中的基础应用，也展示了模块化代码组织在图形程序开发中的实际价值。

---

## 二、项目结构

```text
CG-Lab/
├─ src/
│  └─ Work0/
│     ├─ __init__.py
│     ├─ config.py
│     ├─ physics.py
│     └─ main.py
├─ .gitignore
├─ .python-version
├─ README.md
├─ main.py
├─ pyproject.toml
└─ uv.lock