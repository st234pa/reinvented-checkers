import React, { FunctionComponent } from 'react';
import { Container, Content, Text } from 'native-base';

type HomeProps = {};

const Home: FunctionComponent<HomeProps> = (props: HomeProps) => {
  return (
    <Container>
      <Content padder>
        <Text>yerr</Text>
      </Content>
    </Container>
  );
};

export default Home;
