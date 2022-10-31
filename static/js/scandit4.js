
ScanditSDK.configure("AWZx/z06H+mOAj5WYjawUbAXwJZoCGikHli9zHNCOzfJMpie4G7U0uFifGxRV37Mz0Bi85ltt84BWpVMEV6TS2x7gtTWVy9AFlWqa9liZG6AaEhjoxHzpUsbO2mULARBtWtml/1Urui7dPLKTGI6jzYiiPm2YUnCN1Epab9emXxMWsXCoXShkCVlxaUSCPO8DnT8isR+0Hd2UJNkHFQfGKFqNH+jUXEHXSm+XW9Honsye7/AH3sIi4x2xRu1TDLCD36M1yF/gEIzXDHxPWagKk5VABduNDJ9c205bvldZoJ9ffxRHiq6xRl1jftSY1HUAXzNl8VGHWRxSjJ1A09iDLpGj5/IWu6Hog/Q30NO9VmIWGlP+V/D60I4cvMbfZZm0Rq8w5w2oBlfQCRyAC0E6bx+gy5WHbbhpCFprINjCpk8WxqqIS6moFtRFhl9A+H0zRWNb+JB5uDfbODhakxtneV2aiOFRHD0iuHDHla6oswUMy2mxrGzGCSPvpgMSuxBIQQc/ajxTqDazXFBKWh0thh/PEwU84ulUkRwm5qq+T5SsUwWNTSwqaEx2DYT/keTjjLNhqbGXxacwbAJU9nYKD8ZhJPSTCsc47jmHytZv2cfW9fBEEi7mtP/c8ao0NB27Esq+1biC7/FRcLZ9aSFC9AxE0WQj/HPTegTr034R6DK1DvdST3gIjxVqaZhuRMGd55EjvY/aua9Jq4DzChYoG4AhL9aK1AhOtpAd4CRs1Xw/4uIWM6+UvxWDm6kWHxrkzcHkf+neTlzhRI3zp+gRXmAnkMM8gPbWJHzH//wBe8ye3xjePSBLYSSeQdxMIKzS5LkzLgKYHwE45EcoUptMG+kQAsqKRJDRoqu5jJwGvii6L7ZVVhOYbwLVRfxc205l7u1Mx7Tz3bONNW4recgyJmxe1Qop/IFKCRbbIUzmvYlfpwvB6NW9/JZgmR6Rs8pyrNofxzDX2zvPqhHh+ApLZjTurOmQQ76D8LKHpUb6cMBbhr8FdOk259Sjo0Wegd7MfGx8tEoIsUU5sJLi17xid4UH4o8Ku3jGH82O9xSwzRMpltKA07dT9VQf85Wuk3rfP9UJS2g17KiW2XUTI7/nKZzXNu50MTToQzcPdDLxIWh5tPNIizBYD1QYtM6GePilw==", {
  engineLocation: "https://cdn.jsdelivr.net/npm/scandit-sdk@5.x/build/",
})
  .then(() => {
    return ScanditSDK.BarcodePicker.create(document.getElementById("scandit-barcode-picker"), {
      // enable some common symbologies
	enabledSymbologies: [ScanditSDK.Barcode.Symbology.EAN8, ScanditSDK.Barcode.Symbology.EAN13],
	playSoundOnScan: true,
	vibrateOnScan: true,
    });
  })
  .then((barcodePicker) => {
	// testing our own canvas style
	const canvas = document.querySelector('#theCanvas');
	ctx = canvas.getContext('2d');
	canvas.width = screen.width;
	canvas.height = screen.height;	
	var clearInterval = setInterval(function(){ctx.clearRect(0,0,screen.width,screen.height);},1500);

	// Scandit setup
	var scanSettings = new ScanditSDK.ScanSettings({
	  enabledSymbologies: ["ean8", "ean13", "upca", "upce", "code128", "code39", "code93", "itf", "data-matrix"],
	  codeDuplicateFilter: 1000,
	  maxNumberOfCodesPerFrame : 20
	});
	barcodePicker.applyScanSettings(scanSettings);
    // barcodePicker is ready here, show a message every time a barcode is scanned
    barcodePicker.on("scan", (scanResult) => {


	// Draw on our canvas to highlight the barcodes.
	// TODO: Convert from Scandit location coordinates to Canvas coordinates.
	// TODO: keep dict of scanned codes with expiry time for highlight (so don't duplicate highlights)
	ctx.fillStyle = 'rgba(0,0,255,0.1)';
	var loc = scanResult.barcodes[0].location;
	var x = loc.topLeft.x;
	var y = loc.topLeft.y;
	var width = loc.topRight.x - loc.topLeft.x;
	var height = loc.bottomRight.y - loc.topRight.y;
	ctx.fillRect(x,y,width,height);
	
//	context.fillStyle = "#ff0000"; //<======= here
//	ctx.font = "10px Impact";
///	ctx.fillText(scanResult.barcodes[0].data,x,y);

	//alert('loc:'+x+','+y+', w:'+width+', height:'+height);
	//ctx.fillRect(loc.topLeft.x,loc.topLeft.y,loc.topLeft.x-loc.bottomRight.x,loc.topLeft.y-loc.bottomright.y);
// Create a temporary div

    });
  });

