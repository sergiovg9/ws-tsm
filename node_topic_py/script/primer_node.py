#!/usr/bin/ python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        self.counter_=0
        super().__init__("python_test")
        self.get_logger().info("Hello ROS 2")
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.counter_+=1
        self.get_logger().info("Hello"+str(self.counter_))

def main(args=None):
    rclpy.init(args=args)
    node=MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()