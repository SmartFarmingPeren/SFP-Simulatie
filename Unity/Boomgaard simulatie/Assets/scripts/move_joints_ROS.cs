using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// using ROSMSG = RosMessageTypes.HelloWorld.String;
using RosMessageTypes.Ur10EMoveitConfig;
using ROSMSG = RosMessageTypes.Ur10EMoveitConfig.UR10eJoints;
// using ROSMSG = RosMessageTypes.Ur10EMoveitConfig.UR10eMoveitJoints;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;

public class move_joints_ROS : MonoBehaviour
{
    public GameObject ur10e;

    private int numRobotJoints = 6;
    // private readonly Quaternion pickOrientation = Quaternion.Euler(90, 90, 0);

    // Articulation Bodies
    private ArticulationBody[] jointArticulationBodies;

    // Start is called before the first frame update
    void Start()
    {
        ROSConnection.instance.Subscribe<ROSMSG>("JointsMover", JointsUpdate);

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
    // private void Update()
    // We cant edit the target of the joint directly but we can edit the complete xDrive
    void JointsUpdate(ROSMSG msg)
    {
        Debug.Log(msg);

        /*ArticulationDrive jointArticulationDrive = jointArticulationBodies[0].xDrive;

        // place the target in each jointArticulationDrive
        jointArticulationDrive.target = (float)msg.joint_00;

        // replace joint xDrive with jointArticulationDrive
        jointArticulationBodies[0].xDrive = jointArticulationDrive;*/

        ArticulationDrive joint0 = jointArticulationBodies[0].xDrive;
        ArticulationDrive joint1 = jointArticulationBodies[1].xDrive;
        ArticulationDrive joint2 = jointArticulationBodies[2].xDrive;
        ArticulationDrive joint3 = jointArticulationBodies[3].xDrive;
        ArticulationDrive joint4 = jointArticulationBodies[4].xDrive;
        ArticulationDrive joint5 = jointArticulationBodies[5].xDrive;

        joint0.target = (float)msg.joint_00;
        joint1.target = (float)msg.joint_01;
        joint2.target = (float)msg.joint_02;
        joint3.target = (float)msg.joint_03;
        joint4.target = (float)msg.joint_04;
        joint5.target = (float)msg.joint_05;

        jointArticulationBodies[0].xDrive = joint0;
        jointArticulationBodies[1].xDrive = joint1;
        jointArticulationBodies[2].xDrive = joint2;
        jointArticulationBodies[3].xDrive = joint3;
        jointArticulationBodies[4].xDrive = joint4;
        jointArticulationBodies[5].xDrive = joint5;
    }
}
