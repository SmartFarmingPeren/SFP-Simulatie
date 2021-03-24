using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class kar_camera_no_controller : MonoBehaviour
{
    public float speed = (float)0.1;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 position = this.transform.position;
        if (Input.GetKey("i"))
        {
            position.x = position.x - speed;
        }
        if (Input.GetKey("j"))
        {
            position.z = position.z - speed;
        }
        if (Input.GetKey("k"))
        {
            position.x = position.x + speed;
        }
        if (Input.GetKey("l"))
        {
            position.z = position.z + speed;
        }
        this.transform.position = position;
    }
}
