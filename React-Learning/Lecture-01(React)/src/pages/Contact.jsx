import React, { useState } from 'react'
import Header from '../common/Header'

function Contact() {
  let [formData,setFormdata]=useState(
  {
    uname: '',
    uemail: '',
    uphone: '',
    uaddres: '',
    // index: ''
  });

  let[userData,setUserdata]=useState([]);

  let getValue=(event)=>{
    let inputName=event.target.name;
    let inputValue=event.target.value;
    let oldData={...formData};
    oldData[inputName]=inputValue;
    setFormdata(oldData);
  };

  let handleSubmit=(event)=>{
    event.preventDefault();

    let oldUserData=[...userData,formData]
    setUserdata(oldUserData)
  };
  
  return (
    <>
    <Header/>
    <div>
        <h1>Contact</h1>
        <div className='w-full h-full flex justify-center'>
          <form onSubmit={handleSubmit}  className='w-[800px] pb-5 shadow-2xl rounded-md border border-solid border-[rgba(0,0,0,0,3)]'>
            <h1 className='text-center text-[25px] font-bold'>Form</h1>
            <div className='mt-5 w-full pl-5 pr-5 flex flex-col '>
              <label className='text-[20px] font-bold'>Name :</label>
              <input name='uname' onChange={getValue} value={formData.uname} className='w-full h-10 border border-solid my-2 p-2 outline-none' placeholder='Enter Your Name here'></input>
            </div>
            <div className='mt-5 w-full pl-5 pr-5 flex flex-col '>
              <label className='text-[20px] font-bold'>Email :</label>
              <input name='uemail' onChange={getValue} value={formData.uemail} className='w-full h-10 border border-solid my-2 p-2 outline-none' placeholder='Enter Your Email here'></input>
            </div>
            <div className='mt-5 w-full pl-5 pr-5 flex flex-col '>
              <label className='text-[20px] font-bold'>Phone :</label>
              <input name='uphone' onChange={getValue} value={formData.uphone} className='w-full h-10 border border-solid my-2 p-2 outline-none' placeholder='Enter Your Phone here'></input>
            </div>
            <div className='mt-5 w-full pl-5 pr-5 flex flex-col '>
              <label className='text-[20px] font-bold'>Addres :</label>
              <input name='uaddres' onChange={getValue} value={formData.uaddres} className='w-full h-20 border border-solid my-2 p-2 outline-none' placeholder='Enter Your Addrese here'></input>
            </div>
            <div className='w-full flex justify-center'>
              <button className='w-20 h-10 rounded-lg border border-solid mt-5 bg-slate-300 cursor-pointer'>{formData.index!==''?'Submit':'Save'}</button>
            </div>
          </form>
        </div>
    </div>
    </>
  )
}

export default Contact