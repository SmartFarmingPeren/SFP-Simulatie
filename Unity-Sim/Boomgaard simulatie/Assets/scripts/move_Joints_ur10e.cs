using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RosMessageTypes.Ur10EMoveitConfig;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;

public class move_Joints : MonoBehaviour
{
    public GameObject ur10e;

    private int numRobotJoints = 6;
    private readonly Quaternion pickOrientation = Quaternion.Euler(90, 90, 0);

    // Articulation Bodies
    private ArticulationBody[] jointArticulationBodies;

    // Start is called before the first frame update
    void Start()
    {
        //ROSConnection.instance.Subscribe<UR10eJoints>("JointsMover", JointsUpdate);

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
    void JointsUpdate(UR10eJoints msg)
    {
        UR10eJoints jointInformation = new UR10eJoints();

        ArticulationDrive move = jointArticulationBodies[0].xDrive;
        move.target = (float)60.0;
        jointArticulationBodies[0].xDrive = move;


        /*var jointPositions = msg.trajectories[poseIndex].joint_trajectory.points[jointConfigIndex].positions;
        float[] result = jointPositions.Select(r => (float)r * Mathf.Rad2Deg).ToArray();

        var joint1XDrive = jointArticulationBodies[0].xDrive;
        joint1XDrive.target =*/
        /*
                // Place joints into message
                jointArticulationBodies[0].xDrive.target = jointInformation.joint_00;
                jointArticulationBodies[1].xDrive.target = jointInformation.joint_00;
                jointArticulationBodies[2].xDrive.target = jointInformation.joint_00;
                jointArticulationBodies[3].xDrive.target = jointInformation.joint_00;
                jointArticulationBodies[4].xDrive.target = jointInformation.joint_00;
                jointArticulationBodies[5].xDrive.target = jointInformation.joint_00;*/
    }
}
