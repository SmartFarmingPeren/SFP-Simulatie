using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RosMessageTypes.Ur10EMoveitConfig;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;

public class publish_arm_target : MonoBehaviour
{
    // ROS Connector
    private ROSConnection ros;

    // Variables required for ROS communication
    public string topicName = "JointsPublisher";

    public GameObject ur10e;
    public GameObject target;

    private int numRobotJoints = 6;
    private readonly Quaternion pickOrientation = Quaternion.Euler(90, 90, 0);

    // Articulation Bodies
    private ArticulationBody[] jointArticulationBodies;

    // Start is called before the first frame update
    void Start()
    {
        // Get ROS connection static instance
        ros = ROSConnection.instance;

        // Find and store the joints in jointArticulationBodies
        jointArticulationBodies = new ArticulationBody[numRobotJoints];
        string shoulder_link = "world/base_link/shoulder_link";
        jointArticulationBodies[0] = ur10e.transform.Find(shoulder_link).GetComponent<ArticulationBody>();

        string upper_arm_link = shoulder_link + "/upper_arm_link";
        jointArticulationBodies[1] = ur10e.transform.Find(upper_arm_link).GetComponent<ArticulationBody>();

        string forearm_link = upper_arm_link + "/forearm_link";
        jointArticulationBodies[2] = ur10e.transform.Find(forearm_link).GetComponent<ArticulationBody>();

        string wrist_1_link = forearm_link + "/wrist_1_link";
        jointArticulationBodies[3] = ur10e.transform.Find(wrist_1_link).GetComponent<ArticulationBody>();

        string wrist_2_link = wrist_1_link + "/wrist_2_link";
        jointArticulationBodies[4] = ur10e.transform.Find(wrist_2_link).GetComponent<ArticulationBody>();

        string wrist_3_link = wrist_2_link + "/wrist_3_link";
        jointArticulationBodies[5] = ur10e.transform.Find(wrist_3_link).GetComponent<ArticulationBody>();
    }

    // Update is called once per frame
    //void Update()
    public void Publish()
    {
        UR10eMoveitJoints jointInformation = new UR10eMoveitJoints();

        // Place joints into message
        jointInformation.joint_00 = jointArticulationBodies[0].xDrive.target;
        jointInformation.joint_01 = jointArticulationBodies[1].xDrive.target;
        jointInformation.joint_02 = jointArticulationBodies[2].xDrive.target;
        jointInformation.joint_03 = jointArticulationBodies[3].xDrive.target;
        jointInformation.joint_04 = jointArticulationBodies[4].xDrive.target;
        jointInformation.joint_05 = jointArticulationBodies[5].xDrive.target;

        // place Target Pose into message
        jointInformation.target_X = target.transform.position.x;
        jointInformation.target_Y = target.transform.position.y;
        jointInformation.Target_Z = target.transform.position.z;


        // Send the message to server_endpoint.py running in ROS
        ros.Send(topicName, jointInformation);
    }
}
