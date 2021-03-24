using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ur10_movable : MonoBehaviour
{
    private Vector3 car_movement;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        car_movement = this.transform.parent.parent.parent.position;
        car_movement.y = 3;
        this.transform.position = car_movement;
    }
}
