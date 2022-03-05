from rclpy.node import Node
from std_msgs.msg import *

class MinimalSub():
    def __init__(self, node, name='MinimalSub', msgsType=String, topic='miniSub'):
        self.node = node
        self.name = name
        self.msgsType = msgsType
        self.topic = topic
        self.subscription = self.node.create_subscription(
            self.msgsType,
            self.topic,
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.node.get_logger().info('I heard: "%s"' % msg.data)
