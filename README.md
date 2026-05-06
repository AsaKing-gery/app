# Multi-Robot Agent System

多机器人代理系统，基于 FastAPI 构建，用于管理和协调多个机器人的状态、任务分配和冲突检测。

## 项目结构

```
app/
├── agents/
│   ├── scheduler_agent.py   # 任务调度代理
│   ├── state_agent.py       # 状态管理代理
│   └── strategy_agent.py    # 策略决策代理
├── iot/
│   └── mqtt_sim.py          # MQTT模拟器
├── models/
│   └── robot_state.py       # 机器人状态模型
└── main.py                  # FastAPI主应用
```

## 功能特性

- **状态管理**: 实时追踪所有机器人的位置、电量和工作状态
- **任务分配**: 智能分配任务给合适的机器人执行
- **冲突检测**: 检测机器人位置冲突，避免碰撞发生

## 技术栈

- Python 3.8+
- FastAPI
- MQTT (物联网通信)

## 安装依赖

```bash
pip install fastapi uvicorn paho-mqtt
```

## 快速开始

启动 FastAPI 服务：

```bash
uvicorn main:app --reload
```

服务将在 `http://localhost:8000` 启动。

## API 接口

### 更新机器人状态

**POST** `/update`

参数：
- `robot_id`: 机器人 ID
- `battery`: 电量 (0-100)
- `x`: X 坐标
- `y`: Y 坐标
- `status`: 状态 (IDLE/BUSY/CHARGING)

示例：
```bash
curl -X POST "http://localhost:8000/update?robot_id=robot1&battery=80&x=10&y=20&status=IDLE"
```

### 分配任务

**POST** `/assign_task`

参数：
- `task`: 任务描述

示例：
```bash
curl -X POST "http://localhost:8000/assign_task?task=deliver_package"
```

### 检查冲突

**GET** `/check_conflict`

检查所有机器人是否存在位置冲突。

示例：
```bash
curl http://localhost:8000/check_conflict
```

## 项目架构

```
┌─────────────────────────────────────────────────────────────┐
│                      FastAPI Server                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐   │
│  │ StateAgent  │  │SchedulerAgent│  │ StrategyAgent     │   │
│  │ (状态管理)  │  │  (任务调度)   │  │ (冲突检测策略)    │   │
│  └──────┬──────┘  └──────┬───────┘  └────────┬──────────┘   │
│         │                 │                    │              │
│         └─────────────────┼────────────────────┘              │
│                           ▼                                  │
│                ┌─────────────────┐                           │
│                │   RobotState    │                           │
│                │  (机器人状态模型)│                           │
│                └─────────────────┘                           │
└─────────────────────────────────────────────────────────────┘
```

## License

MIT License
