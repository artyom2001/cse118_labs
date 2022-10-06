using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 
public class Pen : MonoBehaviour
{
    ArrayList points = new ArrayList();
    public GameObject Ball;
    // Start is called before the first frame update
    void Start()
    {
       
    }
 
    // Update is called once per frame
    void Update()
    {
        RaycastHit hit;
 
        bool buttonA = OVRInput.Get(OVRInput.RawButton.A);
        bool buttonB = OVRInput.Get(OVRInput.RawButton.B);
       
        Vector3 position = OVRInput.GetLocalControllerPosition(OVRInput.Controller.RTouch);
        Quaternion rotation = OVRInput.GetLocalControllerRotation(OVRInput.Controller.RTouch);
        if (buttonA == true)
        {
            if (Physics.Raycast(position, transform.TransformDirection(Vector3.forward), out hit))
            {
                Debug.Log("Did Hit");
            }
        }
        //if(buttonA == true)
        //{
        //   Instantiate(Ball, position, rotation);
        //}
    }
}
