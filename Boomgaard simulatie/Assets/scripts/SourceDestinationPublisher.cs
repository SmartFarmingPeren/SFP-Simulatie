using RosMessageTypes.Ur10MoveitConfig;
using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;

public class SourceDestinationPublisher : MonoBehaviour
{
    // ROS Connector
    private ROSConnection ros;

    // Variables required for ROS communication
    public string topicName = "SourceDestination_input";

    public GameObject ur10;
    public GameObject target;
    public GameObject targetPlacement;

    private int numRobotJoints = 6;
    private readonly Quaternion pickOrientation = Quaternion.Euler(90, 90, 0);

    // Articulation Bodies
    private ArticulationBody[] jointArticulationBodies;

    /// <summary>
    /// 
    /// </summary>
    void Start()
    {
        // Get ROS connection static instance
        ros = ROSConnection.instance;

        jointArticulationBodies = new ArticulationBody[numRobotJoints];
        string shoulder_link = "world/base_link/shoulder_link";
        jointArticulationBodies[0] = ur10.transform.Find(shoulder_link).GetComponent<ArticulationBody>();

        string upper_arm_link = shoulder_link + "/upper_arm_link";
        jointArticulationBodies[1] = ur10.transform.Find(upper_arm_link).GetComponent<ArticulationBody>();

        string forearm_link = upper_arm_link + "/forearm_link";
        jointArticulationBodies[2] = ur10.transform.Find(forearm_link).GetComponent<ArticulationBody>();

        string wrist_1_link = forearm_link + "/wrist_1_link";
        jointArticulationBodies[3] = ur10.transform.Find(wrist_1_link).GetComponent<ArticulationBody>();

        string wrist_2_link = wrist_1_link + "/wrist_2_link";
        jointArticulationBodies[4] = ur10.transform.Find(wrist_2_link).GetComponent<ArticulationBody>();

        string wrist_3_link = wrist_2_link + "/wrist_3_link";
        jointArticulationBodies[5] = ur10.transform.Find(wrist_3_link).GetComponent<ArticulationBody>();
    }

    public void Publish()
    {
        NiryoMoveitJoints sourceDestinationMessage = new NiryoMoveitJoints();

        sourceDestinationMessage.joint_00 = jointArticulationBodies[0].xDrive.target;
        sourceDestinationMessage.joint_01 = jointArticulationBodies[1].xDrive.target;
        sourceDestinationMessage.joint_02 = jointArticulationBodies[2].xDrive.target;
        sourceDestinationMessage.joint_03 = jointArticulationBodies[3].xDrive.target;
        sourceDestinationMessage.joint_04 = jointArticulationBodies[4].xDrive.target;
        sourceDestinationMessage.joint_05 = jointArticulationBodies[5].xDrive.target;

        // Pick Pose
        sourceDestinationMessage.pick_pose = new RosMessageTypes.Geometry.Pose
        {
            position = target.transform.position.To<FLU>(),
            orientation = Quaternion.Euler(90, target.transform.eulerAngles.y, 0).To<FLU>()
        };

        // Place Pose
        sourceDestinationMessage.place_pose = new RosMessageTypes.Geometry.Pose
        {
            position = targetPlacement.transform.position.To<FLU>(),
            orientation = pickOrientation.To<FLU>()
        };

        // Finally send the message to server_endpoint.py running in ROS
        ros.Send(topicName, sourceDestinationMessage);
    }
}
