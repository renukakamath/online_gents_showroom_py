<?php include 'admin_header.php';



if (isset($_POST['seller'])) {
	extract($_POST);

	$q="insert into login values(null,'$uname','$pwd','seller')";
	$id=insert($q);
	$q="insert into seller values(null,'$id','$aname','$place','$Phone','$email')";
	insert($q);
	alert('successfully');
	return  redirect('admin_addseller.php');
}




 ?>
   
<!-- ======= Hero Section ======= -->
<section id="hero" class="d-flex align-items-center justify-content-center" >
    <div class="container" data-aos="fade-up">

      <div class="row justify-content-center" data-aos="fade-up" data-aos-delay="150">
        <div class="col-xl-6 col-lg-8">


<font size="4" face="Lato"  style="color: #FFC541">


<H4>ADD Sellers </H4>
<BR>
		<table class="table" style="width: 500px;color: white">
			<tr>
				<th>Seller name</th>
				<td><input type="text" class="form-control" required=""  name="aname"></td>
			</tr>
			
			<tr>
				<th>Place</th>
				<td><input type="text" class="form-control" required=""  name="place"></td>
			</tr>
			
			<tr>
				<th>Phone</th>
				<td><input type="text" class="form-control" required=""  name="Phone"></td>
			</tr>
			<tr>
				<th>Email</th>
				<td><input type="email" class="form-control" required=""  name="email"></td>
			</tr>
			<tr>
				<th>User name</th>
				<td><input type="text" class="form-control" required=""  name="uname"></td>
			</tr>
			<tr>
				<th>Password</th>
				<td><input type="password" class="form-control" required=""  name="pwd"></td>
			</tr>
			<tr>
				<td align="center" colspan="2"><input type="submit" class="btn btn-success" name="seller"></td>
			</tr>
		</table>
	</form>
</center>

</div>
      </div>
    </div>
  </section><!-- End Hero -->

  <main id="main">


<center>

<H4>Sellers</H4>
</font>
<font size="4" face="Lato">
<form method="post">

  <table class="table" style="width: 1300px">
    <tr>
      <th>Seller name</th>
      <th>Place</th>
      <th>Phone</th>
      <th>Email</th>
         </tr>

     <?php 
     $q=" SELECT * FROM `seller`";
      $res11=select($q);
        foreach ($res11 as $row) { ?>

          <tr>
            <td><?php echo $row['seller_name']; ?></td>
            <td><?php echo $row['place']; ?></td>
            <td><?php echo $row['phone'] ?></td>
            <td><?php echo $row['email'] ?></td>
            
         
            <!-- <td>
              <a href="?id1=<?php echo $row['cat_id']; ?>"class="btn btn-success" >ACTIVE</a>
            </td> -->
            
        

                        
                        </tr>
          
      <?php }
      
     ?>
         

  </table>
</center>



{% include 'footer.html'%}