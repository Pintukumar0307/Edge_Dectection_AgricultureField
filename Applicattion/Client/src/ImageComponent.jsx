
import './ImageComponent.css';
import React, { useState } from 'react';
import axios from 'axios';

const ImageComponent = () => {

  const [selectedFile, setSelectedFile] = useState(null);
  const [imageSrc, setImageSrc] = useState('');
  const [area,setArea]=useState();
 

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);


  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!selectedFile) {
      alert('Please select an image');
      return;
    }

    const formData = new FormData();
    formData.append('image', selectedFile);

    try {
      const response = await axios.post('http://localhost:5000/whole_area', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setImageSrc(`data:image/jpg;base64,${response.data.result_image}`);
      setArea(response.data.area_m);
      
    } catch (error) {
      console.error('Error:', error);
    }
  };
 
  // const [resultImage, setResultImage] = useState(null);

  // // const handleImageChange = (e) => {
  // //   setInputImage(URL.createObjectURL(e.target.files[0]));
  // // };
  // const handleImageChange = (e) => {
  //   const file = e.target.files[0];

  //   const Reader = new FileReader();
  //   Reader.readAsDataURL(file);

  //   Reader.onload = () => {
  //     if (Reader.readyState === 2) {
  //       setInputImage(Reader.result);
  //     }
  //   };
  // };

  // const handleSubmit = async () => {

  //   const formData = new FormData();
  //   formData.append('image', inputImage);


  //   try {
  //     const response = await axios.post('http://127.0.0.1:5000/process-image', inputImage , {

  //       headers: {
  //         'Content-Type': 'application/json'
  //       }

  //     });

  //     setResultImage(response.data);

  //   } catch (error) {
  //     console.error('Error processing image:', error);
  //   }
  // };



  return (
    <>
     <div className='heading'>
     <h2>Calculating Cultivated Field Area Using Field Boundaries for Better Farm Management</h2>
     </div>
      
      <div className='image'>
     
    <div className="image-component">
     
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <div className='before-image'>
      {selectedFile && (
             <img src={URL.createObjectURL(selectedFile)} alt="Input" />
           )}
      </div>
     
      <button onClick={handleSubmit}>Process Image</button>
      
    </div>
    <div className='result-component'>
      <div className='result-heading'>
        <h3>Result Image</h3>
      </div>
     
        <div className="result-container">
          {imageSrc && <img src={imageSrc} alt="Processed Image" />}
        </div>
        <div className='area'>
          {area && <h3>Area: {area} metre square</h3>}
          
        </div>
      
    </div>

    </div>
    </>
  );
};

export default ImageComponent;
