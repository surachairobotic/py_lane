import rclpy
from py_lane.minimal_pub import *
from py_lane.minimal_sub import *

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('minimal_publisher')
    
    my_pub = MinimalPub(node)
    my_sub = MinimalSub(node=node, topic='miniPub')

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
