<?php
    $term = json_decode($_POST['data']);
    wp_update_term($term->id, 'local-music', array(
        'location': $term->location
    ));
?>