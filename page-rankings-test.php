<?php 
  //Sorting from functions.php
  add_action( 'pre_get_posts', 'change_sort_order' ); 
  function change_sort_order(&$query){
      if (isset($_POST['cs_action']) && $_POST['cs_action'] == 'custom_sort_order'){
          global $wp;
          if (isset($wp->query_vars["CU_Order"])){
              $query->set( 'order', $wp->query_vars["CU_Order"] );
          }
      }
  }


  add_filter('query_vars', 'add_custom_order_query_vars');
  function add_custom_order_query_vars($vars) {
      // add CU_Order to the valid list of variables
      $new_vars = array('CU_Order');
      $vars = $new_vars + $vars;
      return $vars;
  }

?>

<?php
  /*
   *NEW decay filter
   */
  add_filter('posts_orderby', 'custom_decay_order');
  function custom_decay_order($post) {
        //Getting post age
        $cur_time = date('U');
        //$post_time = get_post_time('U');
        $post_time = 
        $age_hours = ($cur_time - $post_time)/(60*60);

        //Getting order/grade attribute
        //A = 430, F = 0
        $max_order = 430; //A
        $default_order = $max / 2;
        if (empty($post->menu_order)) {
          $post->menu_order = $default_order;
        }
        $grade = $post->menu_order;

        //TODO: Getting pageviews
        $views = 100;

        //Getting pre-decay score
        $predecay = ($views * grade) / $max_order; 

        //Setting score based on decay
        $gravity = 0.5;
        $offset_hours = 24;

        return hn_score($predecay, $age_hours, $gravity, $offset_hours);
  }

  //The two decay functions use the same syntax for passing in argument
  function hn_score($score, $age, $gravity, $offset) {
    if ($age >= $offset) {
      return $score / pow($age-$offset, $gravity);
    }
    else {
      return $score;
    }
  }

  function newton_score($temperature, $hours, $cooling_rate, $offset) {
    if ($hours >= $offset) {
      return $temperature * exp(-$cooling_rate * $hours);
    }
    else {
      return $temperature
    }
  }

  /* 
   * Init filter to get posts
   * All the below works, just uncomment the add_filter and remove_filter
   */
  
  //add_filter( 'posts_orderby', 'order_by_multiple' );

  $args = array(
    'post_type' => array( 'post', 'news' ),
    'posts_per_page' => 10
  );

  query_posts( $args );

  //remove_filter( 'posts_orderby', 'order_by_multiple' );
?>

<?php
//Skeleton
function get_age() {

}

?>

<?php $i = 1; while (have_posts()) : the_post(); ?>
  <div class="grid-3<?php if($i === 4) echo ' last'; ?> entry-content">

    <a href="<?php the_permalink() ?>">

    <?php
    $args = [
      'width' => 270,
      'height' => 193,
      'crop' => 1,
      'background_fill' => 'solid'
    ];
    the_post_thumbnail( $args );
    ?>

    <div class="single-title"><?php echo $found_posts; ?><h3><?php the_title(); ?></h3></div></a>
    <div class="date"><?php echo get_the_date(); ?></div>
    <div class="age">
      <?php
        //Getting post age
        $cur_time = date('U');
        $post_time = get_post_time('U');
        $age_hours = ($cur_time - $post_time)/(60*60);
        //$age = (strtotime(date('U')) - strtotime(get_post_time('U')))/60;
        //echo "Post age: ".$cur_time."-".$post_time."/60";
        echo "Post age: ".$age_hours." hours";

        //Getting order/grade
        //Getting pageviews
      ?>
  </div>

<?php $i++; endwhile; ?>
