using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SoundManager : MonoBehaviour
{

    public static AudioClip FlappyPeturd;
    static AudioSource audioSrc;

    // Start is called before the first frame update
    void Start()
    {
        FlappyPeturd = Resources.Load<AudioClip> ("FlappyPeturd");

        audioSrc = GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public static void PlaySound(string clip)
    {
        switch(clip)
        {
        case "FlappyPeturd":
            audioSrc.loop = true;
            break;
        
        }
    }
}
