<?php

  add_filter( 'posts_orderby', 'order_by_date' );

  $args = array(
    'post_type' => array( 'post', 'news' ),
    'posts_per_page' => 10
  );

  query_posts( $args );

  remove_filter( 'posts_orderby', 'order_by_multiple' );
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
  </div>

<?php $i++; endwhile; ?>
