using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class placeholder_boom_script : MonoBehaviour
{
    public Vector3 newscale = Vector3.one * 4;
    Vector3 ofset = Vector3.zero;

    private Object[] trees;
    GameObject treeobject;

    // Start is called before the first frame update
    void Start()
    {
        ofset.x = 9.98f;
        ofset.z = -9.94f;

        // load all the tree objects into trees and pick one to render
        trees = Resources.LoadAll(path:"treefolder/prefab");

        int treepick = Random.Range(1, trees.Length + 1) - 1;
        treeobject = (GameObject)Instantiate(trees[treepick]);

        // place the tree in the correct postion
        treeobject.transform.parent = this.transform.parent;
        treeobject.transform.position = this.transform.position + ofset;
        treeobject.transform.localScale = newscale;

        this.gameObject.GetComponent<Renderer>().enabled = false;
    }

    // Update is called once per frame
    void Update()
    {

    }
}
