from rclpy.node import Node
from std_msgs.msg import *
from sensor_msgs.msg import PointCloud2
from py_lane.numpy_pc2 import *
from py_lane.minimal_pub import *
import time

class PointCouldHandler():
    def __init__(self, node, name='MinimalSub', msgsType=String):
        self.node = node
        self.subscription = self.node.create_subscription(
            PointCloud2,
            '/camera/depth/color/points',
            self.cb_camPC2,
            10)
        self.subscription  # prevent unused variable warning
        self.i = 1
        self.pub = MinimalPub(node, name, PointCloud2, '/agribot/lane_pc2')
        self.xyzList = []
        
        timer_period = 0.1  # seconds
        self.timer = self.node.create_timer(timer_period, self.timer_callback)        
        
        self.start_t = time.time()

    def timer_callback(self):
        if time.time()-self.start_t < 1.0:
            return -1
        self.xyzList = []
        self.start_t = time.time()

    def cb_camPC2(self, msg):
        '''
        self.node.get_logger().info('I heard: "%s"' % self.i)
        self.i = self.i+1

        self.node.get_logger().info('height : "%s"' % msg.height)
        self.node.get_logger().info('width : "%s"' % msg.width)
        self.node.get_logger().info('is_bigendian : "%s"' % msg.is_bigendian)
        self.node.get_logger().info('point_step : "%s"' % msg.point_step)
        self.node.get_logger().info('row_step : "%s"' % msg.row_step)
        self.node.get_logger().info('is_dense : "%s"' % msg.is_dense)
        self.node.get_logger().info('header : "%s"' % msg.header)
        self.node.get_logger().info('fields : "%s"' % msg.fields)
        
        x = [msg.data[0], msg.data[4], msg.data[8], msg.data[16]]
        self.node.get_logger().info('x["%d"] : "%s, "' % (len(x), x))
        '''      
        xyz = pointcloud2_to_xyz_array(msg)
        x = xyz[:, 0]
        y = xyz[:, 1]
        z = xyz[:, 2]
        self.xyzList.append(xyz)
        self.start_t = time.time()

        #self.node.get_logger().info('type(xyzrgb) = "%s", len: %d, shape: "%s"' % (type(xyz), len(xyz), xyz.shape))
        '''
        self.node.get_logger().info('x[%.2f, %.2f, %.2f], y[%.2f, %.2f, %.2f], z[%.2f, %.2f, %.2f]: %s, %s, %s' % 
            (x.min(), x.max(), x.mean(),
             y.min(), y.max(), y.mean(),
             z.min(), z.max(), z.mean(),
             x.shape, y.shape, z.shape))
        '''
        #self.node.get_logger().info('z : %5.2f\t\t%5.2f\t\t%5.2f' % (z.min(), z.max(), z.mean()))
        
        #new_pc2 = array_to_xyz_pointcloud2f(xyz, frame_id='world')
        #self.pub.publish(new_pc2)

        #for i in range(len(xyz)):
        #    self.node.get_logger().info('xyzrgb[%d] = "%s, type: %s"' % (i, xyz[i], type(xyz[i])))


