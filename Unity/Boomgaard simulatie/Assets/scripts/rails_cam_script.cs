using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class rails_cam_script : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 position = this.transform.position;
        Vector3 origin = Vector3.zero;
        Vector3 rotation = Quaternion.Euler(0f, 0.01f, 0f) * Vector3.up;

        if (Input.GetKey("k"))
        {
            this.transform.position = RotatePointAroundPivot(position, origin, rotation);
        }
        if (Input.GetKey("l"))
        {
            this.transform.position = RotatePointAroundPivot(position, origin, -rotation);
        }

        Vector3 target = Vector3.zero;
        target.y = 10;
        transform.LookAt(target);
    }

    Vector3 RotatePointAroundPivot(Vector3 point, Vector3 pivot, Vector3 angles)
    {
        Vector3 dir = point - pivot; // get point direction relative to pivot
        dir = Quaternion.Euler(angles)* dir; // rotate it
        point = dir + pivot; // calculate rotated point
        return point; // return it
    }
}
