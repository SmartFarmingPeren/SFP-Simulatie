using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using ROSMSG = RosMessageTypes.HelloWorld.String;

public class LikeAndSubscribeToMyROSTopic : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        ROSConnection.instance.Subscribe<ROSMSG>("HelloWorld", Shout);
    }

    // Update is called once per frame
    void Shout(ROSMSG msg)
    {
        Debug.Log(msg.message);
    }
}
